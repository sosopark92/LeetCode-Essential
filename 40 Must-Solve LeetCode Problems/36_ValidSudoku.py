# Determine if a 9 x 9 Sudoku board is valid. 
# Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

from typing import List

class Solution:
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     res = []
    #     for i in range(9):
    #         for j in range(9):
    #             element = board[i][j]
    #             if element != '.':
    #                 res += [(i, element), (element, j), (i // 3, j // 3, element)]

    def isValidSudoku(self, board):

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                box_idx = (i // 3) * 3 + j // 3 # box-index = [[1,2,3],[4,5,6],[7,8,9]]

                if val in rows[i] or val in cols[j] or val in boxes[box_idx]:
                    return False

                rows[i].add(val)
                cols[j].add(val)
                boxes[box_idx].add(val)

        return True
                
            
        