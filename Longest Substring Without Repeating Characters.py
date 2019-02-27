class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        ans, start, end = 0, 0, 0
        countDict = {}
        for i in s:
            end += 1
            countDict[i] = countDict.get(i, 0) + 1
            while countDict[i] > 1:
                countDict[s[start]] -= 1
                start += 1
            ans = max(ans, end - start)
        return ans
