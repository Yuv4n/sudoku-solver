# Sudoku solver

A Python backtracking solver for 9 × 9 Sudoku that always branches on the empty cell with the fewest legal digits (minimum remaining values).

- **Design:** parsing and rule checks in `board.py`, recursive search in `solver.py`. The search works on a copy, so the input grid is never modified.
- **Tests:** eight unit tests, including an invalid grid and a hard puzzle.

## Run

Python 3.9+, standard library only:

```sh
PYTHONPATH=src python3 -m sudoku_solver            # solves the included sample
PYTHONPATH=src python3 -m sudoku_solver puzzle.txt # 81 cells; - 0 . are blanks; "-" reads stdin
PYTHONPATH=src python3 -m unittest discover -s tests
```

## Limits

Returns the first solution found and does not check uniqueness. No benchmark is included. See the [design notes](docs/plan.md).

[MIT licence](LICENSE)
