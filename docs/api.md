# API Specification  
**WLM‑SLP World Interpreter**

This document defines the public API for the **WLM‑SLP World Interpreter**,  
which converts natural‑language world descriptions into deterministic  
**SLP (Structure Language Protocol)** structural graphs.

The API is intentionally minimal:

> **One input → One output → Fully deterministic SLP**

---

# 1. High‑Level API

## `interpret(text: str) -> str`

Convert a natural‑language world description into SLP.

### Signature
```python
def interpret(text: str) -> str:
    """
    Convert a world description into SLP.
    Returns SLP text (RSG or FRSG).
    """
```

### Parameters

| Name | Type | Description |
|------|------|-------------|
| `text` | `str` | Natural‑language description of a scene, world state, or agent observation |

---

### Returns

| Type | Description |
|------|-------------|
| `str` | Deterministic SLP text (RSG or FRSG) |

---

### Raises

| Error | Condition |
|-------|-----------|
| `ValueError` | Empty or invalid input |
| `ParseError` | Input cannot be parsed into world primitives |
| `MappingError` | Extracted primitives cannot be mapped to SLP |
| `EmitError` | SLP generation failed |

---

# 2. Extended API (Optional)

These functions are exposed for advanced users and internal tooling.

---

## `parse(text: str) -> ParsedWorld`

Extract raw world primitives from natural language.

**Output includes:**
- entities  
- attributes  
- relations  
- spatial cues  
- temporal cues  
- action frames  

---

## `extract(parsed: ParsedWorld) -> WorldModel`

Normalize and canonicalize world primitives.

**Output includes:**
- canonical entity list  
- normalized relations  
- resolved attributes  
- inferred dimensions  

---

## `map(world: WorldModel) -> SLPGraph`

Convert normalized world model into SLP structural primitives.

**Output includes:**
- nodes  
- attributes  
- relations  
- states  
- dimensions  
- closure states  

---

## `emit(graph: SLPGraph) -> str`

Emit deterministic SLP text.

**Output:**
- RSG (Resolved Structural Graph)  
- FRSG (Fully Resolved Structural Graph)  

---

# 3. CLI

A simple command‑line interface is provided.

### Interpret a file
```bash
slp-world interpret scene.txt
```

### Interpret inline text
```bash
slp-world interpret "A robot is carrying a box."
```

### Output to file
```bash
slp-world interpret scene.txt --out world.slp
```

---

# 4. Example

### Input
```
A red ball is on the table.
A cat is watching it from the chair.
The window is open.
```

### Code
```python
from slp_world_interpreter import interpret

slp = interpret("""
A red ball is on the table.
A cat is watching it from the chair.
The window is open.
""")

print(slp)
```

### Output
```slp
node Ball {
    color: red
    position: on(Table)
}

node Cat {
    state: watching(Ball)
    position: on(Chair)
}

node Window {
    state: open
}
```

---

# 5. Error Handling

All errors follow a consistent structure:

```json
{
  "error": {
    "type": "MappingError",
    "message": "Failed to map relation: watching(it)",
    "location": "mapper.py:42"
  }
}
```

**Error types:**
- `ValueError`
- `ParseError`
- `ExtractionError`
- `MappingError`
- `EmitError`

---

# 6. Determinism Guarantees

The API guarantees:

- Same input → same output  
- Order‑independent parsing  
- No probabilistic variation  
- No LLM‑dependent randomness  
- Full SLP grammar compliance  
- FRSG‑safe output  

Suitable for:

- agents  
- simulators  
- world models  
- multi‑agent systems  
- reasoning engines  

---

# 7. Versioning

Semantic versioning:

- **0.x** — internal alpha  
- **1.0** — public stable release  
- **1.x** — backward‑compatible improvements  
- **2.0** — breaking changes  

SLP protocol version is tracked separately.

---

# Summary

The **WLM‑SLP World Interpreter API** provides a clean, deterministic,  
production‑ready interface for converting natural‑language world descriptions  
into SLP structural graphs.

It is the first practical bridge between:

> **World → Structure → Reasoning → Action**
