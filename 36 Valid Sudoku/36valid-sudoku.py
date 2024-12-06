class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        column = defaultdict(set)
        square = defaultdict(set)

        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row[i] or board[i][j] in column[j] or board[i][j] in square[(i//3, j//3)]:
                    return False
                row[i].add(board[i][j])
                column[j].add(board[i][j])
                square[(i//3, j//3)].add(board[i][j])
        return True            