
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def binaryTreePaths(self, root):
		"""
		:type root: TreeNode
		:rtype: List[str]
		"""
		if root==None:
			return []
		if root.right==None and root.left==None:
			return [str(root.val)]
		paths=self.binaryTreePaths(root.left)+self.binaryTreePaths(root.right)
		for index in range(len(paths)):
			paths[index]=str(root.val)+"->"+paths[index]
		return paths

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
	p=listToTreeNode([1,2,3,'null',5])
	print(Solution().binaryTreePaths(p))