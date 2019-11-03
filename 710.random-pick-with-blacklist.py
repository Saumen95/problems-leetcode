#
# @lc app=leetcode id=710 lang=python3
#
# [710] Random Pick with Blacklist
#

# @lc code=start
class Solution:
    
    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.N = N
        self.blacklist = blacklist
        self.blacklist.sort()

    def pick(self):
        """
        :rtype: int
        """
        
        import random
        
	# we have N numbers and len(blacklist) is blackedout, so effectively we are randomly picking one number out of M numbers
        M = self.N-len(self.blacklist)
        r = random.randint(0, M-1)
        
	# use binary search to find the maximum index from blacklist such that blacklist[index] < r + index + 1
        start=0
        end=len(self.blacklist)-1
        while(start<=end):
            mid=start+(end-start)//2
            if self.blacklist[mid] < r+mid+1:
                start=mid+1
            elif self.blacklist[mid] >= r+mid+1:
                end=mid-1
            
        return r+start

# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
# @lc code=end

