
class Solution(object):
	def increasingTriplet(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		a, b = float('inf'), float('inf')
		for n in nums:
			if n < a:
				a = n
			elif a < n < b:
				b = n
			elif n > b:
				return True

		return False

print(Solution().increasingTriplet([2,1,5,0,3]))
