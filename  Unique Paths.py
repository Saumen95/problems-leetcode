class Solution:
    # @return an integer
    def fac(self, n):
        if n == 1 or n == 0:
            return 1
        return n * self.fac(n - 1)

    def uniquePaths(self, m, n):
        if m == 1 or n == 1:
            return 1
        val1 = self.fac(m + n - 2)
        val2 = self.fac(m - 1)
        val3 = self.fac(n - 1)
        result = val1 / (val2 * val3)
        return result
