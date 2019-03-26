# -_-看不懂！！！！！！！！！！！！！
class Solution:
	def largestRectangleArea(self, heights):

		"""
		:type heights: List[int]
		:rtype: int
		"""
		# 考虑高度与宽度的最优解
		"""
		思路：这道题跟LeetCode 11很相似，但是因为考虑柱子宽度，因此解题技巧不相同，此题考查单调栈的应用。
		我们首先在数组最后加入0，这是为了方便处理完数组中的所有高度数据。假设存储高度坐标的栈为stack，当
		前处理的高度坐标为i(i∈[0→n])：① 如果当前stack为空，或者heights[i]大于等于栈顶坐标对应高度，则
		将i加入stack中；② 如果heights[i]小于栈顶坐标对应高度，说明可以开始处理栈内的坐标形成的局部递增高
		度，以求得当前最大矩形面积。弹出当前栈顶坐标 = top，此时栈顶新坐标 = top'，那么对应计算面积的
		宽度w = i - 1 - top'（若弹出栈顶坐标后，stack为空，则对应w = i），得到面积s = heights[top] * w，
		此时将i减一（因为进入循环i会加一，而待会儿需要重复考察第i个高度）；③ 遍历完成i∈[0→n]，返回最大矩形面积。

		"""

		i = 0
		max_value = 0
		stack = []  # 思路：利用单调栈，这个栈里面只存储递增或者递减的数组（即这个柱状图的下标）
		heights.append(0)

		while i < len(heights):

			if len(stack) == 0 or heights[stack[-1]] <= heights[i]:  #stack[-1]栈顶元素，单调递增栈
				stack.append(i)
				i += 1
			else:
				now_idx = stack.pop()

				if len(stack) == 0:
					max_value = max(max_value, i * heights[now_idx])
				else:
					max_value = max(max_value, (i - stack[-1] - 1) * heights[now_idx])

		return max_value

if __name__=='__main__':
	s=Solution()
	heights=[2,1,5,6,2,3]
	print(s.largestRectangleArea(heights))