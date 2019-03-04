class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        w = 0
        while(n > 0):
            w = w + n % 2
            n = n / 2
        return w
