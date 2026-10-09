# Sudoku solver

A Python backtracking solver for 9 × 9 Sudoku. I choose the empty cell with the fewest legal digits before branching. Candidate sets exclude digits already used in its row, column and box. The search edits a copy, leaving the supplied grid unchanged.

Parsing and rule checks live in `board.py`; recursive search lives in `solver.py`. The eight existing tests passed during this review, including an invalid grid and a difficult puzzle. The sample command-line run also completed. Previous timing estimates were removed because they were single-run observations, not a saved benchmark.

## Solve a puzzle

Python 3.9+ and the standard library, from this folder:

```sh
PYTHONPATH=src python3 -m sudoku_solver
PYTHONPATH=src python3 -m sudoku_solver puzzle.txt
PYTHONPATH=src python3 -m unittest discover -s tests
```

The first command solves the included sample. A file must contain 81 cells; whitespace is ignored and `-`, `0` or `.` marks a blank. Use `-` as the filename to read stdin. Optional installation with `python3 -m pip install -e .` provides the `sudoku-solver` command.

The solver returns the first solution; it does not check uniqueness. Direct library callers should supply a 9 × 9 integer grid. [Design notes](docs/plan.md) describe the remaining ideas.

[MIT licence](LICENSE)
