#
# @lc app=leetcode id=1014 lang=python3
#
# [1014] Best Sightseeing Pair
#

# @lc code=start
class Solution:
    def maxScoreSightseeingPair(self, a: List[int]) -> int:
        max_so_far,result = a[0],0
        for i in range(1,len(a)):
            result = max(result, max_so_far + a[i] - i)
            max_so_far = max(max_so_far, a[i] + i)

        return result    
# @lc code=end

