# Example: Scene Description → SLP

This example shows how the WLM‑SLP World Interpreter converts a simple scene
description into a deterministic SLP structural graph.

---

## Input (natural language)

```
A red ball is on the table.
A cat is watching it from the chair.
The window is open.
```

---

## Python Usage

```python
from slp_world_interpreter import interpret

text = """
A red ball is on the table.
A cat is watching it from the chair.
The window is open.
"""

slp = interpret(text)
print(slp)
```

---

## CLI Usage

```bash
slp-world interpret scene.txt
```

Where `scene.txt` contains the input text.

---

## Output (SLP)

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

This SLP graph can be passed directly into:

```bash
slp resolve world.slp
slp run world.slp --until-stable
```
