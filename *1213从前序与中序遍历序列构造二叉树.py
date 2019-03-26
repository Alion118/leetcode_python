# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 20:03
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
#前序遍历顺序是遍历根节点，左子树，右子树，而中序遍历则是左子树，根节点，右子树

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def buildTree(self, preorder, inorder):
		if inorder==[]:
			return None
		root = TreeNode(preorder[0])
		#print(preorder,inorder)
		x = inorder.index(root.val)#找到根在中序中的位置
		root.left=self.buildTree(preorder[1:x+1],inorder[0:x])
		root.right=self.buildTree(preorder[x+1:],inorder[x+1:])
		return root

if __name__=='__main__':
	preorder = [3, 9, 20, 15, 7]
	inorder = [9, 3, 15, 20, 7]
	print(Solution().buildTree(preorder,inorder))