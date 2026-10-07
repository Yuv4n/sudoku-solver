import unittest

from sudoku_solver import is_valid, parse, solve

PUZZLE = """
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
SOLUTION = """
5 1 6 3 7 2 4 8 9
4 7 8 6 1 9 5 2 3
3 2 9 5 4 8 1 7 6
7 6 3 8 5 4 2 9 1
1 9 4 2 3 7 8 6 5
2 8 5 9 6 1 7 3 4
8 4 7 1 9 6 3 5 2
6 5 1 7 2 3 9 4 8
9 3 2 4 8 5 6 1 7
"""
HARD = "8........" "..36....." ".7..9.2.." ".5...7..." "....457.." "...1...3." "..1....68" "..85...1." ".9....4.."


class ParseTest(unittest.TestCase):
    def test_accepts_blank_styles(self):
        self.assertEqual(parse("-" * 81), parse("0" * 81))
        self.assertEqual(parse("." * 81), parse("0" * 81))

    def test_rejects_bad_input(self):
        for bad in ["", "1" * 80, "x" * 81]:
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                parse(bad)


class SolveTest(unittest.TestCase):
    def test_solves_known_puzzle(self):
        self.assertEqual(solve(parse(PUZZLE)), parse(SOLUTION))

    def test_does_not_mutate_input(self):
        grid = parse(PUZZLE)
        solve(grid)
        self.assertEqual(grid, parse(PUZZLE))

    def test_hard_puzzle_gives_valid_complete_grid(self):
        result = solve(parse(HARD))
        self.assertTrue(is_valid(result))
        self.assertTrue(all(v for row in result for v in row))

    def test_already_solved(self):
        self.assertEqual(solve(parse(SOLUTION)), parse(SOLUTION))

    def test_duplicate_givens_rejected(self):
        self.assertIsNone(solve(parse("11" + "-" * 79)))

    def test_unsolvable_returns_none(self):
        # Row 1 needs a 9 in its last cell, but column 9 already holds one.
        grid = "12345678-" + "--------9" + "-" * 63
        self.assertIsNone(solve(parse(grid)))


if __name__ == "__main__":
    unittest.main()
