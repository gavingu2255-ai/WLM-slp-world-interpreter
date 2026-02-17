"""
parser.py — Natural‑language → world‑state primitives (ParsedWorld)

This is the minimal deterministic parser used by the WLM‑SLP World Interpreter.
It extracts:
    - entities (noun phrases)
    - attributes (adjectives)
    - relations (verbs)
    - spatial cues (prepositions)
    - simple pronoun resolution (it → last entity)

This is a rule‑based MVP designed for stability and testability.
"""

import re
from dataclasses import dataclass, field
from typing import List, Dict, Optional


# -----------------------------
# Data structures
# -----------------------------

@dataclass
class Entity:
    name: str
    attributes: Dict[str, str] = field(default_factory=dict)


@dataclass
class Relation:
    subject: str
    verb: str
    obj: Optional[str] = None
    spatial: Optional[str] = None


@dataclass
class ParsedWorld:
    entities: List[Entity]
    relations: List[Relation]


# -----------------------------
# Helpers
# -----------------------------

NOUN_PATTERN = r"\b([A-Za-z]+)\b"
ADJ_PATTERN = r"\b(red|blue|green|large|small|broken|open|closed)\b"
VERB_PATTERN = r"\b(watching|carrying|holding|hiding|running|boiling)\b"
SPATIAL_PATTERN = r"\b(on|under|in|near|behind|next to)\b"


def singularize(word: str) -> str:
    if word.endswith("s"):
        return word[:-1]
    return word


def capitalize(word: str) -> str:
    return word[:1].upper() + word[1:].lower()


# -----------------------------
# Main parser
# -----------------------------

def parse(text: str) -> ParsedWorld:
    """
    Parse natural language into world‑state primitives.

    Returns
    -------
    ParsedWorld
    """

    sentences = re.split(r"[.?!]", text)
    entities: Dict[str, Entity] = {}
    relations: List[Relation] = []

    last_entity = None

    for sent in sentences:
        sent = sent.strip()
        if not sent:
            continue

        # 1. Extract nouns → entities
        nouns = re.findall(NOUN_PATTERN, sent)
        nouns = [n for n in nouns if n.lower() not in ("is", "are", "the", "a", "an", "it")]

        entity_names = []
        for n in nouns:
            canonical = capitalize(singularize(n))
            entity_names.append(canonical)

            if canonical not in entities:
                entities[canonical] = Entity(name=canonical)

        # pronoun resolution: "it" → last entity
        if "it" in sent.lower() and last_entity:
            entity_names.append(last_entity)

        if entity_names:
            last_entity = entity_names[-1]

        # 2. Extract adjectives → attributes
        adjectives = re.findall(ADJ_PATTERN, sent.lower())
        for adj in adjectives:
            if entity_names:
                entities[entity_names[0]].attributes["color" if adj in ("red", "blue", "green") else "state"] = adj

        # 3. Extract verbs → relations
        verbs = re.findall(VERB_PATTERN, sent.lower())
        spatial = re.findall(SPATIAL_PATTERN, sent.lower())

        if verbs:
            verb = verbs[0]
            subject = entity_names[0] if entity_names else None
            obj = entity_names[1] if len(entity_names) > 1 else None

            relations.append(
                Relation(
                    subject=subject,
                    verb=verb,
                    obj=obj,
                    spatial=spatial[0] if spatial else None,
                )
            )

        # 4. Spatial-only sentences
        elif spatial and entity_names:
            relations.append(
                Relation(
                    subject=entity_names[0],
                    verb="position",
                    obj=None,
                    spatial=spatial[0],
                )
            )

    return ParsedWorld(
        entities=list(entities.values()),
        relations=relations,
    )
