class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        xpos = [-1]*n
        board = [['.']*n for _ in range(n)]
        res = []
        
        def dfs(board, xpos, y, n):
            nonlocal res
            
            if y == n:
                res += [''.join(line) for line in board],
                return
          
            for x in range(n):
                for pre_y in range(y):
                    if (x == xpos[pre_y] or
                        y - pre_y == abs(x - xpos[pre_y])):
                        break
                else:
                    board[y][x] = 'Q'
                    xpos[y] = x
                    dfs(board, xpos, y + 1, n)
                    board[y][x] = '.'
        
        dfs(board, xpos, 0, n)
        return res