# -*- coding: utf-8 -*-
# @Time    : 2018/10/7 19:12
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @File    : 两数之和.py
# @Software: PyCharm
import numpy as np
class Solution:
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		len_n=len(nums)
		a=[]  # 元素a1的索引值 # 元素a2的索引值
		for i in range(len_n):
			for ii in range(i+1,len_n):
				if nums[i]+nums[ii]==target:
					a.append([i,ii])
		if len(a)!=0:
			for j in range(len(a)):
				return a[j]
		else:
			return None
	def twoSum_fast(self,nums,target):
		len_n=len(nums)
		nums_np=np.array(nums)
		a=[]  # 元素a1的索引值 # 元素a2的索引值
		for i in range(len_n):
			nums_cut=nums_np[i+1:len_n]
			i2_value=nums_cut[np.where(nums_cut==target-nums_np[i])[0]]
			i2=np.where(nums_np==i2_value)[0]
			if len(i2)!=0:
				for ii in i2:
					a.append([i,ii])
		if len(a)!=0:
			for j in range(len(a)):
				return a[j]
		else:
			return None
	def twoSum_fast2(self,nums,target):
		# 用len()方法取得nums列表长度
		n = len(nums)
		#创建一个空字典
		d = {}  #ii_value:i
		for i in range(n):
			ii_value = target - nums[i]
			#字典d中存在nums[i]时
			if nums[i] in d:  # 寻找key
				return [d[nums[i]],i]
			#否则往字典增加键/值对
			else:
				d[ii_value] = i
			#边往字典增加键key:值value对，边与nums[i]进行对比


if __name__ =='__main__':
	s=Solution()
	nums=[2,7,11,15]
	target=9
	print(s.twoSum_fast2(nums,target))

