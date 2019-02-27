class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):

        m = len(matrix)
        if 0 == m:
            return []
        n = len(matrix[0])
        if 0 == n:
            return []
        arr = []

        round = (min(m, n) + 1) / 2
        for x in range(0, round):
            for y in range(x, n - x):
                arr.append(matrix[x][y])
            for y in range(x + 1, m - x - 1):
                arr.append(matrix[y][n - x - 1])
            if m - 2 * x > 1:
                for y in range(n - x - 1, x - 1, -1):
                    arr.append(matrix[m - x - 1][y])
            if n - 2 * x > 1:
                for y in range(m - x - 2, x, -1):
                    arr.append(matrix[y][x])
        return arr
