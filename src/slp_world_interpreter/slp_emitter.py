"""
slp_emitter.py — SLPGraph → deterministic SLP text

This module emits SLP text from an SLPGraph produced by the mapper.
The output is:
    - deterministic
    - stable across runs
    - sorted alphabetically
    - compliant with SLP syntax (RSG/FRSG)

Supported fields (MVP):
    - attributes
    - states
    - positions
    - closures (future extension)
"""

from dataclasses import dataclass
from typing import List, Dict

from .mapper import SLPGraph, SLPNode


# -----------------------------
# Helpers
# -----------------------------

def indent(line: str, level: int = 1) -> str:
    return " " * 4 * level + line


def emit_node(node: SLPNode) -> str:
    """
    Emit a single SLP node in deterministic order.
    """

    lines: List[str] = []
    lines.append(f"node {node.name} {{")

    # 1. Attributes
    for key in sorted(node.attributes.keys()):
        value = node.attributes[key]
        lines.append(indent(f"{key}: {value}"))

    # 2. States
    for state in sorted(node.states):
        lines.append(indent(f"state: {state}"))

    # 3. Positions
    for pos in sorted(node.positions):
        lines.append(indent(f"position: {pos}"))

    # 4. Closures (future extension)
    for c in sorted(node.closures):
        lines.append(indent(f"closure: {c}"))

    lines.append("}")
    return "\n".join(lines)


# -----------------------------
# Main emitter
# -----------------------------

def emit(graph: SLPGraph) -> str:
    """
    Emit deterministic SLP text from an SLPGraph.

    Rules:
        - nodes sorted alphabetically
        - attributes sorted alphabetically
        - states sorted alphabetically
        - positions sorted alphabetically
        - closures sorted alphabetically
        - blank line between nodes
    """

    node_names = sorted(graph.nodes.keys())
    blocks: List[str] = []

    for name in node_names:
        node = graph.nodes[name]
        blocks.append(emit_node(node))

    return "\n\n".join(blocks)
