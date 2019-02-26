class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_num = 0
        for i in range(len(nums)):
            if nums[i] >= max_num:
                max_num = nums[i]
            else:
                max_num -= 1
            if max_num == 0 and i != len(nums) - 1:
                return False
        return True
