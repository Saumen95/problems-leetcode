class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        result = 0
        n = len(s)
        for i in range(n):
            result = result * 26 + ord(s[i]) - 64
        return result
