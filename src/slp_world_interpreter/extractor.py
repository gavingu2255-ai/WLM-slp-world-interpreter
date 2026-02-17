"""
extractor.py — ParsedWorld → canonical WorldModel

This module normalizes and canonicalizes the primitives extracted by the parser:
    - entity names → canonical form
    - attributes → normalized keys
    - relations → normalized verb + spatial mapping
    - dimensions → extracted from spatial cues

The extractor does NOT perform SLP mapping.
It only produces a clean, canonical world model for the mapper.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional

from .parser import ParsedWorld, Entity as ParsedEntity, Relation as ParsedRelation


# -----------------------------
# Canonical data structures
# -----------------------------

@dataclass
class WorldEntity:
    name: str
    attributes: Dict[str, str] = field(default_factory=dict)


@dataclass
class WorldRelation:
    subject: str
    verb: str
    obj: Optional[str] = None
    spatial: Optional[str] = None


@dataclass
class WorldModel:
    entities: List[WorldEntity]
    relations: List[WorldRelation]


# -----------------------------
# Helpers
# -----------------------------

def canonicalize_name(name: str) -> str:
    """Ensure entity names are capitalized and singular."""
    name = name.strip()
    if not name:
        return name

    # singularize
    if name.endswith("s"):
        name = name[:-1]

    # capitalize
    return name[:1].upper() + name[1:].lower()


def canonicalize_attribute_key(key: str) -> str:
    """Normalize attribute keys."""
    mapping = {
        "color": "color",
        "state": "state",
        "size": "size",
        "material": "material",
    }
    return mapping.get(key, key)


def canonicalize_verb(verb: str) -> str:
    """Normalize verb forms."""
    return verb.lower().strip()


def canonicalize_spatial(spatial: Optional[str]) -> Optional[str]:
    if not spatial:
        return None
    return spatial.lower().replace(" ", "_")


# -----------------------------
# Main extractor
# -----------------------------

def extract(parsed: ParsedWorld) -> WorldModel:
    """
    Convert ParsedWorld → canonical WorldModel.

    This step ensures:
        - entity names are canonical
        - attributes are normalized
        - relations are normalized
        - spatial cues are normalized
    """

    world_entities: Dict[str, WorldEntity] = {}
    world_relations: List[WorldRelation] = []

    # 1. Canonicalize entities
    for ent in parsed.entities:
        canonical_name = canonicalize_name(ent.name)

        world_entities[canonical_name] = WorldEntity(
            name=canonical_name,
            attributes={
                canonicalize_attribute_key(k): v
                for k, v in ent.attributes.items()
            }
        )

    # 2. Canonicalize relations
    for rel in parsed.relations:
        subject = canonicalize_name(rel.subject) if rel.subject else None
        obj = canonicalize_name(rel.obj) if rel.obj else None

        world_relations.append(
            WorldRelation(
                subject=subject,
                verb=canonicalize_verb(rel.verb),
                obj=obj,
                spatial=canonicalize_spatial(rel.spatial),
            )
        )

    return WorldModel(
        entities=list(world_entities.values()),
        relations=world_relations,
    )
