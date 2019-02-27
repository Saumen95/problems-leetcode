class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        first = len(s) - 1
        while first >= 0 and s[first] == ' ':
            first -= 1
        while first >= 0 and s[first] != ' ':
            first -= 1
            count += 1
        return count
