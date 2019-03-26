import collections
class RecentCounter2(object):

	def __init__(self):
		self.pinglist=[]
		self.minindex=0

	def ping(self, t):
		"""
		:type t: int
		:rtype: int
		"""
		self.pinglist.append(t)
		while t>self.pinglist[self.minindex]+3000:
			self.minindex+=1
		return len(self.pinglist)-self.minindex

class RecentCounter:

	def __init__(self):
		self.que = collections.deque()

	def ping(self, t):
		"""
		:type t: int
		:rtype: int
		"""

		while self.que and self.que[0] < t - 3000:
			s = self.que[0]
			self.que.popleft()
		self.que.append(t)
		return len(self.que)


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(3001))
print(obj.ping(3002))