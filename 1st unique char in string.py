class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        ch = []
        for i in set(s):
            if s.count(i) == 1:
                ch.append(s.index(i))
        if len(ch) > 0:
            return min(ch)
        else:
            return -1
