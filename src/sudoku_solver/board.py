"""Board parsing, formatting and rule checks.

A board is a 9x9 list of lists of ints, with ``0`` marking an empty cell.
"""
from __future__ import annotations

from typing import List, Set

Grid = List[List[int]]
SIZE = 9
BLANKS = "-0."


def parse(text: str) -> Grid:
    """Parse 81 cells (whitespace ignored). ``-``, ``0`` or ``.`` mean empty."""
    cells = [c for c in text if not c.isspace()]
    if len(cells) != SIZE * SIZE:
        raise ValueError(f"Expected 81 cells, got {len(cells)}")
    grid = []
    for r in range(SIZE):
        row = []
        for c in cells[r * SIZE:(r + 1) * SIZE]:
            if c in BLANKS:
                row.append(0)
            elif c in "123456789":
                row.append(int(c))
            else:
                raise ValueError(f"Invalid cell: {c!r}")
        grid.append(row)
    return grid


def format_grid(grid: Grid) -> str:
    return "\n".join(" ".join(str(v) if v else "-" for v in row) for row in grid)


def candidates(grid: Grid, r: int, c: int) -> Set[int]:
    """Digits that can legally be placed at ``(r, c)``."""
    used = {grid[r][j] for j in range(SIZE)} | {grid[i][c] for i in range(SIZE)}
    br, bc = 3 * (r // 3), 3 * (c // 3)
    used |= {grid[i][j] for i in range(br, br + 3) for j in range(bc, bc + 3)}
    return set(range(1, 10)) - used


def is_valid(grid: Grid) -> bool:
    """True if no row, column or 3x3 box contains a repeated digit."""
    units = [row for row in grid]
    units += [[grid[i][j] for i in range(SIZE)] for j in range(SIZE)]
    units += [
        [grid[i][j] for i in range(br, br + 3) for j in range(bc, bc + 3)]
        for br in (0, 3, 6)
        for bc in (0, 3, 6)
    ]
    return all(len(filled) == len(set(filled))
               for filled in ([v for v in unit if v] for unit in units))
