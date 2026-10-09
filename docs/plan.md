# Search notes

The original plan was to fill forced cells, then backtrack through ambiguous ones. The implementation uses minimum-remaining-values selection at every recursive step. A cell with one candidate is therefore selected before one with several; there is no separate propagation pass.

Candidates are sets. `experiments/lookup_times.py` compares set membership with list scanning for a missing value. This is a collection microbenchmark, not a Sudoku speed measurement. No saved run supports the previous 1000× claim.

The solver copies the input and returns the first solution. Possible next work is to check uniqueness and validate direct library inputs. Bitmask candidates and hidden-single propagation are ideas, not implemented features.
