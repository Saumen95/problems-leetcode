class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict1 = {}
        for c in s:
            if c in dict1:
                dict1[c] += 1
            else:
                dict1[c] = 1
        b = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
        res = ''
        for item in b:
            res += item[0] * item[1]
        return res
