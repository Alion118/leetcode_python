class Solution(object):
	def rob1(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		last = 0
		now = 0
		for i in nums:
			last, now = now, max(last + i, now)
			# temp=now
		    # now=max(last+i,now)
			# last=now
		return now

	def rob(self,nums):
		dp = []
		if len(nums)==0:
			return 0
		elif len(nums)==1:
			return nums[0]
		else:
			dp.append(nums[0])
			dp.append(max(nums[0], nums[1]))

			for i in range(2, len(nums)):
				dp.append(max(dp[i - 2] + nums[i], dp[i - 1]))
			return dp[-1]


if __name__=='__main__':
	num=[2,7,9,3,1]
	print(Solution().rob(num))