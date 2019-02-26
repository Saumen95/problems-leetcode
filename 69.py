class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        ans = float(x)
        while True:
            tmp = ans
            ans = (ans + x / ans) / 2
            if abs(ans - tmp) < 1:
                break
        return int(ans)
