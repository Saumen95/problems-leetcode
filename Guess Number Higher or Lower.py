class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n

        while left <= right:

            # g =  left + ((right - left) >> 1)

            g = int((right+left)/2)

            if guess(g) == 1:
                left = g+1

            elif guess(g) == -1:
                right = g-1
            else:
                return g

        return left 