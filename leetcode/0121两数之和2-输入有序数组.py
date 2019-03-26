# -*- coding: utf-8 -*-
# @Time    : 2019/1/21 20:01
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm

class Solution:
	def mybad_twoSum(self, numbers, target):
		"""
		:type numbers: List[int]
		:type target: int
		:rtype: List[int]
		"""
		for i in range(len(numbers)):
			if numbers[i]>target:
				break
			t=target-numbers[i]
			if t in numbers[i+1:]:
				j = i+1+numbers[i + 1:].index(t)
				return [i+1,j+1]

	def twoSum(self, numbers, target):
		"""
		:type numbers: List[int]
		:type target: int
		:rtype: List[int]
		"""
		#dic={key1:value1,key2:value2,....}
		dic = dict()
		for index, key in enumerate(numbers):
			sub = target - key
			if sub in dic.keys():
				return [dic[sub] + 1, index + 1]
			else:
				dic[key] = index
		return []


if __name__=='__main__':
	num=[2,3,4]
	target=6
	print(Solution().twoSum(num,target))