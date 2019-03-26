# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 20:31
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution(object):
	def levelOrderBottom(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		# bfs广度优先搜索，不熟悉可以网上参考bfs代码
		if not root:
			return []  # 为空则返回空列表
		queue = [root]  # 使用列表实现队列的功能，首先存储root
		res = []
		while queue:  # 当queue不为空时
			nodes = []  # 存节点，每次循环前置空，每次只装一部分
			node_values = []  # 存节点的值
			for node in queue:
				if node.left:
					nodes.append(node.left)  # 将左子树装入队列中
				if node.right:
					nodes.append(node.right)
				node_values += [node.val]  # 因为每次循环node_values都会置空，所以最终结果保存在res里，node_values只是一小部分结果
			res = [node_values] + res  # 实现从底到顶，node_values放前面.
			queue = nodes  # 将新添加的节点重新赋值给queue
		return res


def buildTree(root, preorder, i):
	if i < len(preorder):
		if preorder[i] == None:
			return None  ###这里的return很重要
		else:
			root = TreeNode(preorder[i])
			# print('列表序号：' + str(i) + ' 二叉树的值：' + str(root.val))
			# 往左递推
			root.left = buildTree(root.left, preorder, 2 * i + 1)  # 从根开始一直到最左，直至为空，
			# 往右回溯
			root.right = buildTree(root.right, preorder, 2 * i + 2)  # 再返回上一个根，回溯右，
			# 再返回根'
			# print('************返回根：', root.val)
			return root  ###这里的return很重要
	return root



if __name__ == '__main__':
	l = [3, 9, 20, None, None, 15, 7]
	root = buildTree(None, l, 0)
	print(Solution().levelOrderBottom(root))
