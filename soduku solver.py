class Solution(object):
    def dfs(self, cur, board, vis_row, vis_col, vis_sub_box):
        if cur == 81:
            return True
        x, y = cur // 9, cur % 9
        if board[x][y] != '.':
            return self.dfs(cur + 1, board, vis_row, vis_col, vis_sub_box)

        for k in range(9):
            sub_index = x // 3 * 3 + y // 3
            if vis_row[x][k] or vis_col[y][k] or vis_sub_box[sub_index][k]:
                continue

            vis_row[x][k] = vis_col[y][k] = vis_sub_box[sub_index][k] = True
            board[x][y] = chr(k + ord('1'))

            if self.dfs(cur + 1, board, vis_row, vis_col, vis_sub_box):
                return True

            board[x][y] = '.'
            vis_row[x][k] = vis_col[y][k] = vis_sub_box[sub_index][k] = False

        return False

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        vis_row = [[False] * 9 for _ in range(9)]
        vis_col = [[False] * 9 for _ in range(9)]
        vis_sub_box = [[False] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                k = ord(board[i][j]) - ord('1')
                sub_index = i // 3 * 3 + j // 3
                vis_row[i][k] = vis_col[j][k] = vis_sub_box[sub_index][k] = True
        self.dfs(0, board, vis_row, vis_col, vis_sub_box)
