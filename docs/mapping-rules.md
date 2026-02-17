# Mapping Rules  
**Natural‑language world descriptions → SLP structural graphs**

This document defines the deterministic mapping rules used by the  
**WLM‑SLP World Interpreter** to convert unstructured world descriptions into  
**SLP (Structure Language Protocol)** constructs.

The mapping process has four stages:

1. Parse natural language into world‑state primitives  
2. Extract entities, relations, attributes, states, and dimensions  
3. Map primitives into SLP nodes and relations  
4. Emit deterministic SLP (RSG/FRSG)

These rules guarantee **consistency**, **predictability**, and **full SLP compliance**.

---

# 1. Entity Mapping

## 1.1 Entity Identification
Every noun phrase becomes a candidate entity.

Examples:
- “a red ball” → `Ball`
- “the cat” → `Cat`
- “two people” → `Person1`, `Person2`

Rules:
- Use canonical singular form (`dogs` → `Dog`)
- Use capitalized identifiers
- If multiple entities of same type appear, index them (`Person1`, `Person2`)

---

## 1.2 Entity Attributes
Adjectives and descriptive phrases become attributes.

Examples:
- “a **red** ball” → `color: red`
- “a **large** dog” → `size: large`
- “a **broken** window” → `state: broken`

Rules:
- Physical descriptors → attributes  
- Conditions → state attributes  
- Colors, sizes, materials → attributes  

---

# 2. Relation Mapping

## 2.1 Spatial Relations
Spatial prepositions map to SLP relations.

| Natural Language | SLP Mapping |
|------------------|-------------|
| on               | `on(X)` |
| under            | `under(X)` |
| in               | `in(X)` |
| near             | `near(X)` |
| behind           | `behind(X)` |
| next to          | `next_to(X)` |

Example:

```
The cat is under the table.
```

→

```slp
node Cat {
    position: under(Table)
}
```

---

## 2.2 Action Relations
Verbs describing interactions become `state:` relations.

Examples:
- “The cat is watching the ball.”  
  → `state: watching(Ball)`
- “The robot is carrying a box.”  
  → `state: carrying(Box)`

Rules:
- Subject = actor  
- Object = target  
- Verb phrase = state relation  

---

## 2.3 Ownership / Possession
Patterns like “has”, “carrying”, “holding” map to possession relations.

Examples:
- “The man has a key.” → `possession: Key`
- “The robot is holding a tool.” → `state: holding(Tool)`

---

# 3. State Mapping

## 3.1 Static States
Adjectival or descriptive states map to `state:`.

Examples:
- “The door is closed.” → `state: closed`
- “The window is open.” → `state: open`

---

## 3.2 Dynamic States
Ongoing actions map to `state: verb(target)`.

Examples:
- “The dog is running.” → `state: running`
- “Two people are arguing.”  
  → `state: arguing(Person2)`  
  → `state: arguing(Person1)`

---

# 4. Dimensional Mapping

## 4.1 Location Dimension
Every entity receives a `location:` dimension if present.

Examples:
- “in the kitchen” → `location: Kitchen`
- “on the chair” → `location: on(Chair)`

---

## 4.2 Temporal Dimension
Temporal cues map to `time:`.

Examples:
- “now” → `time: present`
- “yesterday” → `time: past`
- “soon” → `time: near_future`

---

## 4.3 Agent Perspective Dimension
If the description is from an agent’s viewpoint:

- “I see a box.” → `visibility: visible_to(Self)`
- “I hear footsteps.” → `auditory: footsteps`

---

# 5. Multi‑Entity Mapping

## 5.1 Groups
Plural nouns become indexed individuals unless explicitly grouped.

Example:

```
Three birds are flying.
```

→

```slp
node Bird1 { state: flying }
node Bird2 { state: flying }
node Bird3 { state: flying }
```

---

## 5.2 Symmetric Relations
Relations like “arguing”, “fighting”, “hugging” map symmetrically.

Example:

```
Two people are arguing.
```

→

```slp
node Person1 { state: arguing(Person2) }
node Person2 { state: arguing(Person1) }
```

---

# 6. Closure Mapping

## 6.1 Completed Actions
Perfect tense → closure state.

Examples:
- “The door has closed.” → `closure: closed`
- “The robot has dropped the box.” → `closure: dropped(Box)`

---

## 6.2 Irreversible States
Words like “broken”, “destroyed”, “dead” map to closure.

Examples:
- `closure: broken`
- `closure: destroyed`
- `closure: dead`

---

# 7. Tension Mapping

## 7.1 Conflicts
Words indicating conflict map to tension relations.

Examples:
- “arguing” → `tension: conflict`
- “fighting” → `tension: physical_conflict`

---

## 7.2 Goals / Intentions
Intentions map to tension with direction.

Examples:
- “trying to open the door”  
  → `tension: attempt(open(Door))`

---

# 8. Full Example

### Input
```
Two people are arguing loudly in the kitchen.
A pot is boiling on the stove.
The dog is hiding under the table.
```

### Output
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

# 9. Determinism Guarantee

All mapping rules are:

- deterministic  
- order‑independent  
- grammar‑aligned  
- resolution‑compatible  
- runtime‑safe  

This ensures that **any interpreter implementation** will produce the same SLP graph for the same input.

---

# 10. Notes

- These rules are versioned with SLP v0.9  
- Full FRSG alignment is optional but recommended  
- Future versions will include spatial reasoning and temporal chains  

---

# Summary

This document defines the **complete mapping pipeline** from natural language → SLP.  
It ensures that world descriptions become **stable, explicit, deterministic structural graphs** suitable for reasoning, simulation, and multi‑agent coordination.
