"""
WLM‑SLP World Interpreter — Public API

This module exposes the high‑level `interpret()` function, which converts
natural‑language world descriptions into deterministic SLP (RSG/FRSG).

Pipeline:
    text → parse → extract → map_to_slp → emit → SLP text
"""

from .parser import parse
from .extractor import extract
from .mapper import map_to_slp
from .slp_emitter import emit


class ParseError(Exception):
    """Raised when natural language cannot be parsed into world primitives."""
    pass


class MappingError(Exception):
    """Raised when extracted primitives cannot be mapped to SLP."""
    pass


class EmitError(Exception):
    """Raised when SLP emission fails."""
    pass


def interpret(text: str) -> str:
    """
    Convert a natural‑language world description into deterministic SLP.

    Parameters
    ----------
    text : str
        Natural‑language description of a scene, world state, or agent observation.

    Returns
    -------
    str
        Deterministic SLP text (RSG or FRSG).

    Raises
    ------
    ValueError
        If input is empty or invalid.
    ParseError
        If text cannot be parsed into world primitives.
    MappingError
        If extracted primitives cannot be mapped to SLP.
    EmitError
        If SLP generation fails.
    """

    if not text or not text.strip():
        raise ValueError("Input text is empty.")

    # 1. Parse → world primitives
    try:
        parsed = parse(text)
    except Exception as e:
        raise ParseError(f"Failed to parse input: {e}") from e

    # 2. Extract → canonical world model
    try:
        world = extract(parsed)
    except Exception as e:
        raise MappingError(f"Failed to extract world model: {e}") from e

    # 3. Map → SLP graph
    try:
        graph = map_to_slp(world)
    except Exception as e:
        raise MappingError(f"Failed to map world model to SLP: {e}") from e

    # 4. Emit → deterministic SLP text
    try:
        slp_text = emit(graph)
    except Exception as e:
        raise EmitError(f"Failed to emit SLP: {e}") from e

    return slp_text


__all__ = [
    "interpret",
    "ParseError",
    "MappingError",
    "EmitError",
]
