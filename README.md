# WLM‑SLP World Interpreter  
**Convert world descriptions → deterministic SLP structural graphs**

The **WLM‑SLP World Interpreter** is the first application layer built on top of the  
**Structure Language Protocol (SLP)**.  
It transforms natural‑language world descriptions into **deterministic structural graphs** (RSG/FRSG)  
that can be used by agents, world models, simulators, and reasoning engines.

This library provides the missing layer between **LLMs / world models** and **structured reasoning**:

> **World → Structure → Reasoning → Action**

---

# ✨ Features

## **1. Natural‑language → SLP**
- Parse scenes, world states, video descriptions, agent observations  
- Extract entities, relations, attributes, states, tensions, dimensions  
- Map them into SLP structural primitives  
- Emit deterministic **RSG** or **FRSG** graphs  

## **2. Deterministic structural output**
- No ambiguity  
- No hallucinated relations  
- No unstable schemas  
- Fully aligned with SLP v0.9 specification  

## **3. Clean API for agents & world models**
- One function: `interpret(text)`  
- Returns SLP text ready for:
  - SLP interpreter  
  - SLP resolver  
  - SLP runtime  

## **4. Designed for multi‑agent systems**
Output is compatible with:
- SLP interpreter  
- SLP resolution engine  
- SLP runtime  
- WLM agent frameworks  

---

# 🚀 Quickstart

## **Install**

```bash
pip install slp-world-interpreter
```

---

# 🧪 Python Usage

```python
from slp_world_interpreter import interpret

slp = interpret("""
A robot is carrying a box.
The door is closed.
""")

print(slp)
```

### Output

```slp
node Robot {
    state: carrying(Box)
}

node Box {
}

node Door {
    state: closed
}
```

---

# 🖥 CLI Usage

### Interpret inline text

```bash
slp-world interpret "A robot is carrying a box."
```

### Interpret a file

```bash
slp-world interpret scene.txt
```

### Output to file

```bash
slp-world interpret scene.txt --out world.slp
```

---

# 🧠 Why this exists

LLMs can **describe** the world.  
World models can **predict** the world.  
But neither can **structure** the world.

The WLM‑SLP World Interpreter provides the missing layer:

- Deterministic structure  
- Explicit relations  
- Explicit dimensions  
- Explicit states  
- Explicit closure  
- Explicit tensions  

This enables:

- Stable agent behaviour  
- Reliable planning  
- Transparent reasoning  
- Multi‑agent coordination  
- World‑model alignment  

---

# 📦 API

## `interpret(text: str) → str`

Convert a natural‑language world description into deterministic SLP.

```python
def interpret(text: str) -> str:
    """
    Convert a world description into SLP.
    Returns SLP text (RSG or FRSG).
    """
```

Full API documentation:  
➡ `docs/api.md`

---

# 📘 Examples

## Scene → SLP

**Input**

```
Two people are arguing loudly in the kitchen.
A pot is boiling on the stove.
The dog is hiding under the table.
```

**Output**

```slp
node Person1 {
    state: arguing(Person2)
    volume: loud
    location: Kitchen
}

node Person2 {
    state: arguing(Person1)
    volume: loud
    location: Kitchen
}

node Pot {
    state: boiling
    location: on(Stove)
}

node Dog {
    state: hiding
    location: under(Table)
}
```

More examples:  
- `examples/scene_to_slp.md`  
- `examples/world_state_to_slp.md`  
- `examples/video_description_to_slp.md`  

---

# 🏗 Repository Structure

```
slp-world-interpreter/
│
├── README.md
├── pyproject.toml
├── setup.cfg
│
├── src/
│   └── slp_world_interpreter/
│       ├── parser.py
│       ├── extractor.py
│       ├── mapper.py
│       ├── slp_emitter.py
│       └── api.py
│
├── examples/
│   ├── scene_to_slp.md
│   ├── world_state_to_slp.md
│   └── video_description_to_slp.md
│
├── tests/
│   ├── test_parser.py
│   ├── test_extractor.py
│   ├── test_mapper.py
│   ├── test_emitter.py
│   └── test_end_to_end.py
│
└── docs/
    ├── overview.md
    ├── mapping-rules.md
    ├── api.md
    └── roadmap.md
```

---

# 🔗 Relationship to SLP

This library is fully aligned with:

- SLP syntax  
- SLP grammar  
- SLP interpreter  
- SLP resolution engine  
- SLP runtime  

It outputs valid SLP that can be directly fed into:

```bash
slp interpret world.slp
slp resolve world.slp
slp run world.slp --until-stable
```

---

# 📅 Status

- MVP complete  
- SLP‑compliant  
- Ready for integration with agents, world models, simulators  

Next milestones (see `docs/roadmap.md`):

- Video‑frame → SLP  
- Multi‑agent observation → SLP  
- Real‑time world updates  
- FRSG optimization  

---

# 📄 License

To be finalized with WLM v1.0 governance model.  
Designed for open, non‑enclosable, structurally safe licensing.

---

# 🧩 Summary

The **WLM‑SLP World Interpreter** is the first practical bridge between  
natural‑language world descriptions and deterministic structural reasoning.

It enables:

- Agents that understand structure  
- World models that output structure  
- Simulators that run structure  
- AI systems that reason with structure  

A foundational component of the **WLM ecosystem**.
