class Solution:
	def singleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		return sum(set(nums)) * 2 - sum(nums)

if __name__=='__main__':
	print(Solution().singleNumber([2,3,3,4,5,5,4]))