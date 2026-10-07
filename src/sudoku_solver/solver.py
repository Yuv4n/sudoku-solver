"""Backtracking Sudoku solver.

Each step picks the empty cell with the fewest legal digits (the "minimum
remaining values" heuristic), so forced cells are filled immediately and
dead ends are detected as early as possible.
"""
from __future__ import annotations

from typing import Optional

from .board import SIZE, Grid, candidates, is_valid


def solve(grid: Grid) -> Optional[Grid]:
    """Return a solved copy of ``grid``, or ``None`` if it has no solution."""
    if not is_valid(grid):
        return None
    work = [row[:] for row in grid]
    return work if _search(work) else None


def _search(grid: Grid) -> bool:
    best = None
    for r in range(SIZE):
        for c in range(SIZE):
            if grid[r][c] == 0:
                options = candidates(grid, r, c)
                if not options:
                    return False
                if best is None or len(options) < len(best[2]):
                    best = (r, c, options)
    if best is None:
        return True  # no empty cells left

    r, c, options = best
    for digit in sorted(options):
        grid[r][c] = digit
        if _search(grid):
            return True
    grid[r][c] = 0  # undo before backtracking
    return False
