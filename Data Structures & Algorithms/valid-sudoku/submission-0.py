class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            row = [each for each in board[i] if each!="."]
            if len(set(row))!=len(row):
                return False
        for j in range(9):
            col = []
            for i in range(9):
                val=board[i][j]
                if val!=".":
                    col.append(val)
            if len(set(col))!=len(col):
                return False
        for i in range(0,9,3):
            for j in range(0,9,3):
                grid = []
                for r in range(i,i+3):
                    for c in range(j,j+3):
                        val=board[r][c]
                        if val!=".":
                            grid.append(val)
                if len(set(grid))!=len(grid):
                    return False
        return True
            
