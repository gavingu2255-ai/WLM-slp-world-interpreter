"""
mapper.py — WorldModel → SLPGraph

This module converts a canonical WorldModel into SLP structural primitives:
    - node
    - attributes
    - state
    - position (spatial)
    - closure (future extension)

This is a deterministic rule-based mapper aligned with mapping-rules.md.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .extractor import WorldModel, WorldEntity, WorldRelation


# -----------------------------
# SLP Graph Data Structures
# -----------------------------

@dataclass
class SLPNode:
    name: str
    attributes: Dict[str, str] = field(default_factory=dict)
    states: List[str] = field(default_factory=list)
    positions: List[str] = field(default_factory=list)
    closures: List[str] = field(default_factory=list)


@dataclass
class SLPGraph:
    nodes: Dict[str, SLPNode]


# -----------------------------
# Mapping Helpers
# -----------------------------

def map_attribute(node: SLPNode, key: str, value: str):
    """Map entity attributes to SLP attributes."""
    node.attributes[key] = value


def map_state(node: SLPNode, verb: str, obj: Optional[str]):
    """Map dynamic or static states."""
    if obj:
        node.states.append(f"{verb}({obj})")
    else:
        node.states.append(verb)


def map_position(node: SLPNode, spatial: str, obj: Optional[str]):
    """Map spatial relations to position: on(X), under(X), etc."""
    if obj:
        node.positions.append(f"{spatial}({obj})")
    else:
        node.positions.append(spatial)


# -----------------------------
# Main Mapper
# -----------------------------

def map_to_slp(world: WorldModel) -> SLPGraph:
    """
    Convert a canonical WorldModel into an SLPGraph.

    Rules implemented (MVP):
        - entity → node
        - attributes → node.attributes
        - verb → node.states
        - spatial → node.positions
        - closure (future extension)
    """

    nodes: Dict[str, SLPNode] = {}

    # 1. Create nodes for all entities
    for ent in world.entities:
        nodes[ent.name] = SLPNode(
            name=ent.name,
            attributes=dict(ent.attributes),
            states=[],
            positions=[],
            closures=[],
        )

    # 2. Map relations
    for rel in world.relations:
        if rel.subject not in nodes:
            continue  # safety fallback

        node = nodes[rel.subject]

        # Spatial-only relation
        if rel.verb == "position" and rel.spatial:
            map_position(node, rel.spatial, rel.obj)
            continue

        # Dynamic or static state
        if rel.verb:
            map_state(node, rel.verb, rel.obj)

        # Spatial modifier (e.g., "watching the ball from the chair")
        if rel.spatial:
            map_position(node, rel.spatial, rel.obj)

    return SLPGraph(nodes=nodes)
