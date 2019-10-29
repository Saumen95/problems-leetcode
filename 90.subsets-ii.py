#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()


        def helper(start, sub_res):
            res.append(sub_res[:])

            for i in range(start, n):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                sub_res.append(nums[i])
                helper(i + 1, sub_res)
                sub_res.pop()

        helper(0, [])
        return res    
            

        
# @lc code=end

