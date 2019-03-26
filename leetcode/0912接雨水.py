"""接雨水"""


class Solution:
	def trap(self, height):
		movepeak = 0
		triprain = 0
		maxindex = 0
		for i in range(1, len(height)):
			if height[i] > height[maxindex]:
				maxindex = i
		for i in range(0, maxindex):
			if movepeak < height[i]:
				movepeak = height[i]
			else:
				triprain += movepeak - height[i]
		movepeak = 0

		for j in range(len(height) - 1, maxindex, -1):
			if movepeak < height[j]:
				movepeak = height[j]
			else:
				triprain += movepeak - height[j]
		return triprain


if __name__ == '__main__':
	s = Solution()
	print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))