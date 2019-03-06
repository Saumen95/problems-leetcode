class Solution(object):
	def containsNearbyDuplicates(self, nums, k):
		ky = {}
		if k < 0:
			return False
		if len(nums) < 2:
			return False  # ignoring all impossible cases
		for i in range(2, len(nums)):
				j = ky.get(nums[i])
			    if j != None:
			    	if i-j <= k:
			    		return True
			    ky[nums[i]] = i  # getting nums fits the condition
		return False	    		
								

	
