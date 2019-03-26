class Solution(object):
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""

		# The stack to keep track of opening brackets.
		stack = []

		# Hash map for keeping track of mappings. This keeps the code very clean.
		# Also makes adding more types of parenthesis easier
		mapping = {")": "(", "}": "{", "]": "["}
		for char in s:
			if char in mapping:
				top_element = stack.pop() if stack else '#'
				if mapping[char] != top_element:
					return False
			else:
				stack.append(char)
		return not stack

if __name__=='__main__':
	print(Solution().isValid("(([]){})"))