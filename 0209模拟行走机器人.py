# -*- coding: utf-8 -*-
# @Time    : 2019/2/9 23:18
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
class Solution:
	def robotSim(self, commands, obstacles):
		"""
		:type commands: List[int]
		:type obstacles: List[List[int]]
		:rtype: int
		"""
		dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] #4个梯度方向
		x = y = di = res = 0
		obstacles = set(map(tuple, obstacles))
		# map(tuple,obstacles)把列表转换为元祖
		# 这个利用list检索，代码运行效率较低，将输入的障碍点改为包含tuple的set类型后，提交通过
		for cmd in commands:
			if cmd == -2:
				di = (di - 1) % 4
			elif cmd == -1:
				di = (di + 1) % 4
			else:
				for k in range(cmd):
					if (x + dx[di], y + dy[di]) not in obstacles:
						x += dx[di]
						y += dy[di]

						res = max(res, x * x + y * y)
		return res

if __name__=='__main__':
	print(Solution().robotSim([4,-1,-1],[[]]))