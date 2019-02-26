class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.col = [False] * n
        self.diag = [False] * (2 * n)
        self.anti_diag = [False] * (2 * n)
        self.result = []
        self.recursive(0, n, [])
        return self.result

    def recursive(self, row, n, column):
        if row == n:
            self.result.append(
                list(map(lambda x: '.' * x + 'Q' + '.' * (n - 1 - x), column)))
        else:
            for i in range(n):
                if not self.col[i] and not self.diag[row + i] and not self.anti_diag[n - i + row]:
                    self.col[i] = self.diag[row +
                                            i] = self.anti_diag[n - i + row] = True
                    self.recursive(row + 1, n, column + [i])
                    self.col[i] = self.diag[row +
                                            i] = self.anti_diag[n - i + row] = False


if __name__ == "__main__":
    print(Solution().solveNQueens(5))
