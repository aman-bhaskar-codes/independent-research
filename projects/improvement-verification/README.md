---
id: improvement-verification
title: Improvement Verification Harness
status: planned
programme: ral-programme
created: 2026-10-02
---

# Improvement Verification Harness

**Status:** Planned  
**Programme:** [Reliable Autonomous Learning](../../programmes/ral/README.md)

## Project Brief

This project aims to build an experimental harness to rigorously verify whether an autonomous system's adaptation mechanism produces genuine capability improvement or merely behavioral change (e.g., memorization or evaluator gaming). 

The initial study is deliberately narrow to ensure high observability and rigorous controls.

## Proposed Scope

- **Task Family**: Small, self-contained coding tasks with deterministic, execution-based scoring (e.g., unit tests).
- **Adaptation Mechanism**: Strategy updates derived from environmental feedback (test failures).
- **Control**: A frozen, no-adaptation baseline agent.
- **Evaluation splits**: Strict separation of development tasks (where adaptation occurs) and held-out evaluation tasks (where generalization is measured).

See the [Draft Protocol](protocol.md) for detailed experimental design.

## Directory Structure

- `src/`: Core implementation of the harness.
- `configs/`: Experiment configuration files.
- `experiments/`: Experiment definitions and run scripts.
- `analysis/`: Notebooks and scripts for analyzing results.
- `results/`: Raw outputs and metrics (Note: large files are excluded via `.gitignore`).
- `tests/`: Unit tests for the harness infrastructure.
- `environment/`: Container or sandbox definitions for safe task execution.
