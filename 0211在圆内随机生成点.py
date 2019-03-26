# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 19:40
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
import random


class Solution:
	def __init__(self, radius, x_center, y_center):
		"""
		:type radius: float
		:type x_center: float
		:type y_center: float
		"""
		self.r = radius
		self.x = x_center
		self.y = y_center

	def randPoint(self):
		"""
		:rtype: List[float]
		"""
		dx = random.random() * 2 * self.r
		dy = random.random() * 2 * self.r
		square = self.r ** 2
		if dx ** 2 + dy ** 2 > square:
			return self.randPoint()
		else:
			return [self.x+dx, self.y+dy]


# Your Solution object will be instantiated and called as such:
obj = Solution(radius=2, x_center=1, y_center=1)
print(obj.randPoint())
