class Solution:
    def canPartition(self, nums):
        """
        动态规划，dp[i]记录的是这些数字能否组成i（True or False）
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums)%2 ==1:
            return False

        half_sum = int(sum(nums)/2)
        n = len(nums)
        dp = [False]*(half_sum+1)
        dp[0]=True

        for num in nums:
            for j in range(half_sum,num-1,-1):
                # dp[i]表示不取这个数，dp[i-num]表示取这个数
                dp[j] = dp[j] or dp[j-num]
        return dp[half_sum]

print(Solution().canPartition(nums=[1,5,11,5]))