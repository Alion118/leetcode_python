# -*- coding: utf-8 -*-
# @Time    : 2019/2/10 17:07
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
class Solution:
	def readBinaryWatch_dfs(self, num):
		"""
		:type num: int
		:rtype: List[str]
		"""
		self.dfs(1,num)
		return self.time_list

	def __init__(self):
		self.hour = [1, 2, 4, 8]
		self.minute = [1, 2, 4, 8, 16, 32]
		self.time_list = []
		self.temp  = 0
		self.x = [0 for x in range(10)]

	def num_equal_condition(self,t,num):
		if(t == 10):
			if(self.x[0:t].count(1)==num):
				return True
			else:return False
		else:
			if(self.x[0:t].count(1)<=num):
				return True
			else:return False

	def dfs(self,t,num):
		if t>10:
			time = self.return_time(self.x)
			if(int(time.split(":")[0])<12 and int(time.split(":")[1])<60):
				self.time_list.append(time)
		else:
			for i in [0,1]:
				self.x[t-1] = i
				if(self.num_equal_condition(t,num)):
					self.dfs(t+1,num)

	def return_time(self,x):
		hh = 0
		mm = 0
		for index,h in enumerate(x[0:4]):
			if(h == 1):
				hh+=self.hour[index]
		for index,m in enumerate(x[4:]):
			if(m == 1):
				mm+=self.minute[index]
		if(mm<10):
			return str(hh)+":"+"0"+str(mm)
		else:
			return str(hh)+":"+str(mm)

	def readBinaryWatch(self, num):
		"""
		:type num: int
		:rtype: List[str]
		"""
		res=[]
		for i in range(12):
			for j in range(60):
				if bin(i)[2:].count('1')+bin(j)[2:].count('1')==num:
					res.append("{}:{}".format(i,j if j>=10 else '0'+str(j)))
					# "{}:{}"中大括号是格式化要填的东西
		return res


if __name__=='__main__':
	print(Solution().readBinaryWatch(2))