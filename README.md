# Sudoku Solver

A backtracking Sudoku solver that uses the *minimum remaining values* heuristic: it always fills the cell with the fewest legal digits first, so forced moves are made immediately and dead ends are found early.

## Highlights

- **Heuristic search**: forced cells are resolved instantly, and branching happens only where it must.
- **Input validation**: rejects malformed boards and boards that already break the rules, and reports unsolvable ones.
- **Non-destructive**: returns a new grid and leaves the input untouched.
- **Tested and dependency-free**: 8 unit tests, standard library only.

## Usage

Requires Python 3.9+.

```bash
pip install -e .
sudoku-solver puzzle.txt     # or: PYTHONPATH=src python -m sudoku_solver puzzle.txt
```

A puzzle is 81 cells, with whitespace ignored and `-`, `0` or `.` for blanks. With no argument, a built-in sample is solved; `-` reads from stdin.

As a library:

```python
from sudoku_solver import parse, solve, format_grid

solution = solve(parse(open("puzzle.txt").read()))
print(format_grid(solution) if solution else "No solution")
```

## Performance

Single run on a laptop (Python 3.9):

| Puzzle | Time |
|---|---|
| Sample (included) | 0.01 s |
| Hard puzzle (a well-known difficult 21-clue grid, in the test suite) | ~1 s |

## Project structure

```
src/sudoku_solver/
  board.py        parsing, formatting, candidate and validity checks
  solver.py       backtracking search with MRV cell selection
tests/            unit tests
experiments/      set vs list lookup-time comparison
docs/plan.md      original plan and optimisation notes
```

```bash
PYTHONPATH=src python -m unittest discover -s tests
```

## Possible extensions

Bitmask candidate sets for faster constraint checks; constraint propagation (naked and hidden singles) before branching.

## License

MIT
