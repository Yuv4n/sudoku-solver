"""Usage: python -m sudoku_solver [puzzle.txt]   (reads stdin if no file, or "-")"""
import sys

from .board import format_grid, parse
from .solver import solve

SAMPLE = """
5 - - - - 2 4 - 9
- 7 - - - 9 - - -
3 - - - - 8 - 7 6
- - - 8 - 4 2 9 -
- - - - 3 - 8 - -
- - 5 - - 1 - - -
- 4 7 1 - 6 3 - -
- - - - 2 3 - - 8
9 - - - - 5 - 1 -
"""


def main() -> int:
    if len(sys.argv) > 1:
        path = sys.argv[1]
        text = sys.stdin.read() if path == "-" else open(path).read()
    else:
        text = SAMPLE
    try:
        grid = parse(text)
    except ValueError as err:
        print(f"Invalid puzzle: {err}", file=sys.stderr)
        return 2
    solution = solve(grid)
    if solution is None:
        print("No solution.")
        return 1
    print(format_grid(solution))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
