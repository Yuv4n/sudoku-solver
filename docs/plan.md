# Plan (August 2025)

Two phases:

1. **Simple solver** – fill in the obvious cells (those with a single legal digit).
2. **Recursive solver** – backtracking search for the rest.

## Optimisations considered

- Prioritise cells with the fewest candidates. **Done**: minimum-remaining-values selection in `solver.py`.
- Represent digits as integers and candidate sets as bitmasks, using bit shifts for set operations. *Not yet done.*

## Experiment

`experiments/lookup_times.py` compares membership tests on a set (O(1) average) with a list (O(n)). It motivated tracking candidates as sets: at 10,000 items a list lookup was roughly 1000× slower in my run.
