# WLM‑SLP World Interpreter — Roadmap  
**From natural‑language world descriptions → deterministic structural reasoning**

This roadmap outlines the planned evolution of the **WLM‑SLP World Interpreter**,  
focusing on stability, determinism, multi‑agent alignment, and full SLP ecosystem integration.

The roadmap is divided into three layers:

1. **Core Interpreter Enhancements**  
2. **Structural Reasoning Extensions**  
3. **Ecosystem & Multi‑Agent Integration**

---

# 1. Core Interpreter Enhancements

## 1.1 FRSG Optimization (v0.10 → v0.12)
Improve the FRSG (Fully Resolved Structural Graph) emitter:

- deterministic ordering of nodes  
- canonical attribute sorting  
- stable dimension resolution  
- conflict‑free closure propagation  
- improved error surfaces (ParseError, MappingError, EmitError)

**Goal:**  
Zero nondeterminism across runs, machines, and environments.

---

## 1.2 Spatial Reasoning Module (v0.12 → v0.14)
Add structured spatial inference:

- relative positions (`left_of`, `right_of`, `between`)  
- multi‑object spatial chains  
- room‑level containment  
- implicit spatial inference (“on the counter” → `location: Counter`)  

**Goal:**  
Enable richer world‑state graphs for simulation and robotics.

---

## 1.3 Temporal Reasoning Module (v0.14 → v0.16)
Add temporal chain extraction:

- event ordering  
- tense‑based state transitions  
- temporal dimensions (`time: past`, `time: future`)  
- closure propagation across time  

**Goal:**  
Allow world models to represent evolving states, not static snapshots.

---

# 2. Structural Reasoning Extensions

## 2.1 Dimension Inference Engine (v0.16 → v0.18)
Automatically infer missing dimensions:

- location  
- time  
- agent perspective  
- visibility  
- tension  

**Goal:**  
Fill structural gaps without hallucination or nondeterminism.

---

## 2.2 Multi‑Sentence World Consolidation (v0.18 → v0.20)
Merge multiple descriptions into a single coherent SLP graph:

- entity co‑reference resolution  
- pronoun grounding  
- cross‑sentence relation stitching  
- conflict detection & resolution  

**Goal:**  
Enable paragraph‑level world interpretation.

---

## 2.3 Multi‑Agent Observation Fusion (v0.20 → v0.22)
Combine world descriptions from multiple agents:

- perspective tagging  
- partial‑knowledge merging  
- contradiction detection  
- agent‑specific visibility layers  

**Goal:**  
Support multi‑agent systems and distributed world models.

---

# 3. Ecosystem Integration

## 3.1 Video‑Frame → SLP (v0.22 → v0.26)
Integrate with vision models to convert:

- single frames  
- short clips  
- scene summaries  

into SLP world graphs.

**Goal:**  
Enable simulation engines and agents to operate on structured visual input.

---

## 3.2 Real‑Time World Updates (v0.26 → v0.28)
Support incremental updates:

- streaming observations  
- delta‑based SLP updates  
- state transition tracking  
- conflict‑free merges  

**Goal:**  
Enable real‑time agents and simulators.

---

## 3.3 SLP Runtime Integration (v0.28 → v0.30)
Tight integration with the SLP runtime:

- direct execution of interpreter output  
- runtime‑safe FRSG emission  
- stable world‑state transitions  
- deterministic resolution  

**Goal:**  
Make the interpreter a first‑class component of the SLP execution pipeline.

---

# 4. Long‑Term Vision (v1.0+)

## 4.1 Full World Model Alignment
World models output **structure**, not text:

- SLP‑native world states  
- SLP‑native reasoning traces  
- SLP‑native action plans  

## 4.2 Multi‑Agent Structural Substrate
Agents share:

- the same world graph  
- the same structural substrate  
- the same deterministic reasoning layer  

## 4.3 Simulation‑Ready World States
SLP becomes the universal interface for:

- simulators  
- agents  
- world models  
- reasoning engines  

---

# Summary

The WLM‑SLP World Interpreter roadmap focuses on:

- deterministic structural mapping  
- spatial & temporal reasoning  
- multi‑agent alignment  
- real‑time world updates  
- full SLP ecosystem integration  

A foundational step toward:

> **World → Structure → Reasoning → Action**
