"""
CLI for WLM‑SLP World Interpreter

Usage:
    slp-world interpret "A robot is carrying a box."
    slp-world interpret scene.txt
    slp-world interpret scene.txt --out world.slp
"""

import argparse
import sys
from pathlib import Path

from .api import interpret


def load_text(input_arg: str) -> str:
    """Load text either from inline string or from a file path."""
    p = Path(input_arg)
    if p.exists() and p.is_file():
        return p.read_text(encoding="utf-8")
    return input_arg  # treat as inline text


def cmd_interpret(args):
    text = load_text(args.input)
    slp = interpret(text)

    if args.out:
        Path(args.out).write_text(slp, encoding="utf-8")
    else:
        print(slp)


def main():
    parser = argparse.ArgumentParser(
        prog="slp-world",
        description="WLM‑SLP World Interpreter CLI"
    )

    sub = parser.add_subparsers(dest="command")

    # slp-world interpret ...
    p_interpret = sub.add_parser("interpret", help="Interpret text or file into SLP")
    p_interpret.add_argument("input", help="Inline text or path to a file")
    p_interpret.add_argument("--out", help="Write output to file")
    p_interpret.set_defaults(func=cmd_interpret)

    args = parser.parse_args()

    if not hasattr(args, "func"):
        parser.print_help()
        sys.exit(1)

    args.func(args)
