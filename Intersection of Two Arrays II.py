class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        nums1 = collections.Counter(nums1)
        for x in nums2:
            if x in nums1:
                ans.append(x)
                nums1[x] -= 1
                if nums1[x] == 0:
                    del nums1[x]
        return ans
