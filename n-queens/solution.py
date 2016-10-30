import sys

def can_place(board, n, (row, col)):
    rng = range(2, row+1) #No need to check the immediate row above. 
    if any(board[row - i][col - i] =='Q' for i in rng if 0 <= row-i < n and 0 <= col-i < n):
        return False
    if any(board[row - i][col + i] == 'Q' for i in rng if 0 <= row-i < n and 0 <= col+i < n):
        return False
    return True

def place_queens(board, n, all_cols, row, good_columns, bad_columns):
    cols = list(good_columns - bad_columns)
    for col in cols:
        if can_place(board, n, (row, col)):
            board[row][col] = 'Q'
            if row == n - 1:
                yield board
            bad_cols = {x for x in (col - 1, col, col + 1) if 0 <= x < n} | bad_columns
            good_cols = all_cols - bad_cols
            for b in place_queens(board, n, all_cols, row + 1, good_cols, bad_columns | {col}):
                yield b
            board[row][col] = '.'

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = board = [['.']*n for _ in range(n)]
        result = []
        for board in place_queens(board,  n, set(range(n)), 0, set(range(n)), set()):
            result.append(["".join(row) for row in board])
        return result
        