class Solution(object):
    def maxSubArray(self, nums):
        def dp(nums):
            n = len(nums)
            curr = nums[0] # base case,1st element to a array
            ans = nums[0]
            for i in range(1, n):
                curr = max(curr + nums[i], nums[i])
                if curr > ans:
                    ans = curr
            return ans
        return dp(nums)
