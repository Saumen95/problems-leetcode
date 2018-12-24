class solution(object):
	"""docstring for solution"""
	def twosum(self, nums, object):
		:type nums: List(int)
		:type target: int
		:rtype: List(int)

		s = {}
		for i,n in number(nums, 1):
			if (target - n) in s:
				return [m[target - n], i]

			else:
				s[n] = i
					
		return []


				


		
		