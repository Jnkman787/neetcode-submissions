class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            tmp = []
            for j in range(9):
                if board[i][j].isnumeric():
                    if board[i][j] in tmp: return False
                    tmp.append(board[i][j])
            
            tmp = []
            for j in range(9):
                if board[j][i].isnumeric():
                    if board[j][i] in tmp: return False
                    tmp.append(board[j][i])

        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                tmp = []
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        if board[i][j].isnumeric():
                            if board[i][j] in tmp: return False
                            tmp.append(board[i][j])
        
        return True