class Solution1(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a1 = [-1] * 256
        a2 = [-1] * 256
        for i in range(len(s)):
            if a1[ord(s[i])] != a2[ord(t[i])]:
                return False
            a1[ord(s[i])] = i
            a2[ord(t[i])] = i
        return True
