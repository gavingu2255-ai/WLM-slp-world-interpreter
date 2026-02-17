# Example: World State Update → SLP

This example demonstrates how the interpreter handles world‑state updates,
including dynamic actions and spatial relations.

---

## Input (natural language)

```
The robot is carrying a box.
The box is heavy.
The robot is moving toward the door.
```

---

## Python Usage

```python
from slp_world_interpreter import interpret

text = """
The robot is carrying a box.
The box is heavy.
The robot is moving toward the door.
"""

slp = interpret(text)
print(slp)
```

---

## Output (SLP)

```slp
node Robot {
    state: carrying(Box)
    state: moving(Door)
}

node Box {
    state: heavy
}

node Door {
}
```

---

This output can be fed into any SLP‑compatible agent or simulator.
