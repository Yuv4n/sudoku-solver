#   Yuvan Marimuthu
#   Suduko Solver

#   Suduko Board Solver Simple
board = [
        ["5","-","-","-","-","2","4","-","9"],
        ["-","7","-","-","-","9","-","-","-"],
        ["3","-","-","-","-","8","-","7","6"],
        ["-","-","-","8","-","4","2","9","-"],
        ["-","-","-","-","3","-","8","-","-"],
        ["-","-","5","-","-","1","-","-","-"],
        ["-","4","7","1","-","6","3","-","-"],
        ["-","-","-","-","2","3","-","-","8"],
        ["9","-","-","-","-","5","-","1","-"],]

solved = [
        ["5","1","6","3","7","2","4","8","9"],
        ["4","7","8","6","1","9","5","2","3"],
        ["3","2","9","5","4","8","1","7","6"],
        ["7","6","3","8","5","4","2","9","1"],
        ["1","9","4","2","3","7","8","6","5"],
        ["2","8","5","9","6","1","7","3","4"],
        ["8","4","7","1","9","6","3","5","2"],
        ["6","5","1","7","2","3","9","4","8"],
        ["9","3","2","4","8","5","6","1","7"],]

def simpleSolve(board):
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val == "-":

                choices = {"1","2","3","4", "5","6","7","8","9"}

                choices_ = {"1","2","3","4", "5","6","7","8","9"}
                for row_ in board:
                    if row_[j] != "-":
                        if row_[j] in choices_:
                            if row_[j] in choices:
                                choices.remove(row_[j])
                            choices_.remove(row_[j])
                        else:
                            return False

                choices_ = {"1","2","3","4", "5","6","7","8","9"}
                for el in row:
                    if el != "-":
                        if el in choices_:
                            if el in choices:
                                choices.remove(el)
                            choices_.remove(el)
                        else:
                            return False

                choices_ = {"1","2","3","4", "5","6","7","8","9"}
                for i_ in range(3 * (i//3), 3 * (i//3) + 3):
                    for j_ in range(3 * (j//3), 3 * (j//3) + 3):
                        num = board[i_][j_]
                        if num != "-":
                            if num in choices:
                                choices.remove(num)
                            if num in choices_:
                                choices_.remove(num)
                            else:
                                return False

                if len(choices) == 0:
                    return False
                elif len(choices) == 1:
                    board[i][j] = choices.pop()
                    if simpleSolve(board):           # recurse immediately
                        return True
                    board[i][j] = "-"                # undo if branch fails
                    return False
                else:
                    for choice in choices:
                        board[i][j] = choice          # try a value
                        if simpleSolve(board):        # recurse
                            return True               # solved somewhere below
                    board[i][j] = "-"                 # undo before backtracking
                    return False
    return True

for row in board:
    print(*row)
print("\n")
simpleSolve(board)
print(board == solved)
for row in board:
    print(*row)
print("\n")