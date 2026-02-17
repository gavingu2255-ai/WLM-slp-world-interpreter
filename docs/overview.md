# WLM‑SLP World Interpreter — Overview  
**Natural‑language world descriptions → Deterministic SLP structural graphs**

The **WLM‑SLP World Interpreter** is the first application‑layer module built on top of the  
**Structure Language Protocol (SLP)**.  
Its purpose is simple:

> Convert unstructured world descriptions into **structured, deterministic, machine‑interpretable graphs**.

This enables agents, world models, and simulators to operate on **structure**, not text.

---

## 1. What this library does

The interpreter takes natural‑language descriptions of:

- scenes  
- world states  
- video summaries  
- agent observations  
- environment updates  

and produces **SLP**:

- nodes  
- relations  
- attributes  
- states  
- tensions  
- dimensions  
- closure states  

The output is a valid **RSG** or **FRSG** graph that can be fed directly into:

```bash
slp interpret world.slp
slp resolve world.slp
slp run world.slp --until-stable
```

---

## 2. Why this matters

LLMs and world models can *describe* the world.  
But they cannot:

- structure it  
- stabilize it  
- reason over it  
- maintain consistency  
- track relations  
- track state transitions  
- represent multi‑agent dynamics  

SLP provides the **structural substrate**.  
This interpreter provides the **bridge**.

Together they enable:

- deterministic reasoning  
- stable agent behaviour  
- transparent world updates  
- multi‑agent coordination  
- simulation‑ready world states  

This is the missing layer between:

> **World → Structure → Reasoning → Action**

---

## 3. Architecture

The interpreter is composed of four main modules:

### **1. Parser**
Breaks natural language into world‑state primitives:
- entities  
- actions  
- relations  
- attributes  
- spatial cues  
- temporal cues  

### **2. Extractor**
Normalizes and canonicalizes:
- entity identities  
- relation types  
- state descriptors  
- dimensional markers  

### **3. Mapper**
Maps extracted primitives into SLP constructs:
- `node`  
- `relation`  
- `attribute`  
- `state`  
- `dimension`  
- `closure`  

### **4. SLP Emitter**
Outputs deterministic SLP text:
- RSG (Resolved Structural Graph)  
- FRSG (Fully Resolved Structural Graph)  

---

## 4. Example

### Input
```
A red ball is on the table.
A cat is watching it from the chair.
The window is open.
```

### Output (SLP)
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

## 5. Integration with SLP

The interpreter is fully aligned with:

- SLP syntax  
- SLP grammar  
- SLP interpreter  
- SLP resolution engine  
- SLP runtime  

This means:

- Output is always valid SLP  
- Output can be resolved deterministically  
- Output can be executed in the SLP runtime  
- Output can be used by any SLP‑compatible agent  

---

## 6. Use cases

### 1. Agent world‑state understanding  
Agents can convert observations → structure → decisions.

### 2. World model alignment  
World models can output structured states instead of raw text.

### 3. Simulation engines  
Simulators can ingest SLP graphs directly.

### 4. Multi‑agent systems  
Shared world structure = consistent coordination.

### 5. Reasoning engines  
SLP provides explicit relations and states for deterministic reasoning.

---

## 7. Roadmap (high‑level)

- Video‑frame → SLP  
- Real‑time world updates  
- Multi‑agent observation fusion  
- FRSG optimization  
- SLP dimension inference  
- Spatial reasoning module  
- Temporal reasoning module  

See `docs/roadmap.md` for details.

---

## 8. Summary

The **WLM‑SLP World Interpreter** is the first practical bridge between  
natural‑language world descriptions and deterministic structural reasoning.

It enables:

- structured world understanding  
- stable agent behaviour  
- transparent reasoning  
- simulation‑ready world states  

A foundational component of the **WLM ecosystem**.
