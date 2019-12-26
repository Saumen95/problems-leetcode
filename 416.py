class Solution:
    def canPartition(self, nums):
        nums.sort()
        sums = [nums[0]]
        for i in range(1, len(nums)):
            sums.append(sums[-1] + nums[i])
        if sums[-1] % 2 or nums[-1]*2 > sums[-1]:
            return False
        s = sums[-1] // 2
        
        
        ## dp
        dp = [True] + [False] * s
        for i,x in enumerate(nums):
            for m in range(min(sums[i], s), nums[i]-1, -1):
                dp[m] = dp[m] | dp[m-nums[i]]
                if dp[s]: return True
        return dp[-1]
        