class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        zeros = 0
        safe = 0

        for n in nums:
            if n != 0:
                nums[safe] = n
                safe += 1
            else:
                zeros += 1

        for i in range(zeros):
            nums[safe] = 0
            safe += 1
