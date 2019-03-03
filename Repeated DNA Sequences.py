class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        dict = {}
        for i in range(len(s) - 9):
            key = s[i:i + 10]
            if key not in dict:
                dict[key] = 1
            else:
                dict[key] += 1
        res = []
        for elem in dict:
            if dict[elem] > 1:
                res.append(elem)
        return res
