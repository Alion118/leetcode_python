class Solution:
	def reverse(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		st=str(x)
		li = list(st)
		if li[0] == '-':
			a = li.pop(0)
			li.reverse()
			li.insert(0,a)
			rest = "".join(li)
			answer = int(rest)
			if answer < (-2) ** 31:
				return 0
			return answer
		else:
			li.reverse()
			rest = "".join(li)
			answer = int(rest)
			if answer > (2 ** 31 - 1):
				return 0
			return answer

if __name__=='__main__':
	print(Solution().reverse(-120))