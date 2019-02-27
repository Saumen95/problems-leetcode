class Solution:

    def search(self, nums, target):         """ 
        :type nums: List[int] 
        :type target: int 
        :rtype: int 
        """  
        l = 0   
        r = len(nums) - 1  
        return self.bin_search(l, r, nums, target)  
    def bin_search(self, l, r, nums, target):         m = (l + r) // 2  
        if l > r:             return -1  
        if target == nums[m]:             return m  
        elif target == nums[r]:             return r  
        elif target == nums[l]:             return l  
        else:             if nums[m] < nums[r]:                 if target > nums[m] and target < nums[r]:                     return self.bin_search(m + 1, r, nums, target)  
                else:                     return self.bin_search(l, m - 1, nums, target)  
            else:                 if target < nums[m] and target > nums[l]:                     return self.bin_search(l, m - 1, nums, target)  
                else:                     return self.bin_search(m + 1, r , nums, target) 
