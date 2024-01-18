class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        sub = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board)):

                if board[r][c]=='.':
                    continue
                if board[r][c] in row[r]:
                    return False

                if  board[r][c] in col[c]:
                    return False

                if board[r][c] in sub[(r//3,c//3)]:

                   return False


                row[r].add(board[r][c])
                col[c].add(board[r][c])
                sub[(r//3,c//3)].add(board[r][c])
        
        
        return True