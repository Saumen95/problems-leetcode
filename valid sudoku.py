class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_vis = [[False] * 9 for _ in range(9)]
        col_vis = [[False] * 9 for _ in range(9)]
        sub_box_vis = [[False] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                index = ord(board[i][j]) - ord('1')
                sub_index = i // 3 * 3 + j // 3
                if row_vis[i][index] or col_vis[j][index] or sub_box_vis[sub_index][index]:
                    return False
                row_vis[i][index] = col_vis[j][index] = sub_box_vis[sub_index][index] = True
        return True
