#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        
        new = image[:][:]
        row, col = len(image), len(image[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        q = deque([[sr, sc]])
        color = image[sr][sc]
        
        while len(q):
            x, y = q.popleft()
            new[x][y] = newColor
            for dirc in directions:
                nx, ny = x + dirc[0], y + dirc[1]
                if 0 <= nx < row and 0 <= ny < col and image[nx][ny] == color:
                    q.append([nx,ny])
                    
        return new
# @lc code=end

