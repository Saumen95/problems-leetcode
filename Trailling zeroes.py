class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        check = 5

        while n >= check:
            count += n / check
            check *= 5
        return count


if __name__ == "__main__":
    n = 13
    print Solution().trailingZeroes(n)
