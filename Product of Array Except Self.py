class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res, leftMul, rightMul = [0] * \
            len(nums), [0] * len(nums), [0] * len(nums)
        leftMul[0] = rightMul[len(nums) - 1] = 1
        for i in xrange(1, len(nums)):
            leftMul[i] = leftMul[i - 1] * nums[i - 1]
        for i in xrange(len(nums) - 2, -1, -1):
            rightMul[i] = rightMul[i + 1] * nums[i + 1]
        for i in xrange(len(nums)):
            res[i] = leftMul[i] * rightMul[i]
        return res
