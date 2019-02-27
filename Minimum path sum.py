class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])

        paths = [[] for i in range(m)]

        paths[0].append(grid[0][0])

        for i in range(1, m):
            paths[i].append(paths[i - 1][0] + grid[i][0])

        for j in range(1, n):
            paths[0].append(paths[0][j - 1] + grid[0][j])

        for i in range(1, m):
            for j in range(1, n):
                paths[i].append(min(paths[i][j - 1], paths[i - 1][j])
                                + grid[i][j])

        return paths[m - 1][n - 1]
