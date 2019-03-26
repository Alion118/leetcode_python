# -*- coding: utf-8 -*-
# @Time    : 2019/2/5 19:49
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm

# Definition for a Node.
class TreeNode:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = [] #值
        cur = [root] #循环的根
        while cur:
            next = []
            temp = []
            for node in cur:
                temp.append(node.val)
                next += node.children
            res.append(temp)
            cur = next
        return res

def listToTreeNode(input):
	if not input:
		return None

	root = TreeNode(int(input[0]))
	nodeQueue = [root]
	front = 0
	index = 1
	while index < len(input):
		node = nodeQueue[front]
		front = front + 1

		item = input[index]
		index = index + 1
		if item != "null":
			leftNumber = int(item)
			node.left = TreeNode(leftNumber)
			nodeQueue.append(node.left)

		if index >= len(input):
			break

		item = input[index]
		index = index + 1
		if item != "null":
			rightNumber = int(item)
			node.right = TreeNode(rightNumber)
			nodeQueue.append(node.right)
	return root
if __name__=='__main__':
	print(Solution().levelOrder(listToTreeNode([1,3,2,4,5,6])))