class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
        print(nums)
        if (len(nums) % 2) == 0:
            return (nums[len(nums) / 2 - 1] + nums[len(nums) / 2]) / 2.0
        else:
            return nums[(len(nums) - 1) / 2]
