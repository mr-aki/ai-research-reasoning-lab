# Reasoning Architecture

The long-term reasoning stack separates **generation**, **critique**, **verification**, and **synthesis**.

A typical flow:

1. Retrieve candidate evidence.
2. Generate independent candidate analyses.
3. Ask specialized critics to identify unsupported claims and conflicts.
4. Verify claims against evidence.
5. Synthesize only supported conclusions.
6. Abstain or request more evidence when support is inadequate.
7. Record the complete trace for evaluation.

The current repository implements only transparent, dependency-free building blocks. Model-backed reasoning will be added behind the model interface and measured against explicit baselines.
