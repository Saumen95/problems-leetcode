class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        import collections
        return collections.Counter(s) == collections.Counter(t)

    def isAnagram2(self, s, t):
        return sorted(s) == sorted(t)


if __name__ == '__main__':
    sol = Solution()
    s = "anagram"
    t = "nagaram"
    print sol.isAnagram(s, t)
    print sol.isAnagram2(s, t)
