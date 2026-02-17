# Example: Video Description → SLP

This example shows how a short video description can be converted into
a structured SLP world graph.

---

## Input (natural language)

```
Two people are arguing loudly in the kitchen.
A pot is boiling on the stove.
The dog is hiding under the table.
```

---

## Python Usage

```python
from slp_world_interpreter import interpret

text = """
Two people are arguing loudly in the kitchen.
A pot is boiling on the stove.
The dog is hiding under the table.
"""

slp = interpret(text)
print(slp)
```

---

## Output (SLP)

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

---

This example demonstrates multi‑entity mapping, symmetric relations,
and spatial reasoning.
