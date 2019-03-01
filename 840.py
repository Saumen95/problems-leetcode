import itertools


class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cnt = 0
        height, width = len(grid), len(grid[0])
        if height < 3 or width < 3:
            return 0

        for i in range(height - 2):
            for j in range(width - 2):
                matrix = [row[j: j + 3] for row in grid[i: i + 3]]
                if any(x < 1 or x > 9 for x in itertools.chain(*matrix)):
                    continue

                rows = {sum(matrix[i]) for i in range(3)}

                T = list(itertools.zip_longest(*matrix))
                cols = {sum(T[i]) for i in range(3)}

                diagonal1 = {sum(matrix[i][i] for i in range(3))}
                diagonal2 = {sum(matrix[~i][~i] for i in range(3))}

                if len(rows | cols | diagonal1 | diagonal2) == 1:
                    cnt += 1

        return cnt


grid = [[4, 3, 8, 4],
        [9, 5, 1, 9],
        [2, 7, 6, 2]]
s = Solution()
r = s.numMagicSquaresInside(grid)
print(r)
