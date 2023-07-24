class Node:
	def __init__(self, val):
		self.data = val
		self.left = None
		self.right = None

def hasPathSum(root, targetSum):
	if not root:
		return False
	s = [root]
	sums = [root.data]
	while s:
		node = s.pop()
		sum_val = sums.pop()
		if not node.left and not node.right:
			if sum_val == targetSum:
				return True
		if node.left:
			s.append(node.left)
			sums.append(sum_val + node.left.data)
		if node.right:
			s.append(node.right)
			sums.append(sum_val + node.right.data)
	return False

if __name__ == '__main__':
	root = Node(10)
	root.left = Node(8)
	root.right = Node(2)
	root.left.left = Node(3)
	root.left.right = Node(5)
	root.right.left = Node(2)

	targetSum = 23
	if hasPathSum(root, targetSum):
		print("There is a root-to-leaf path with sum", targetSum)
	else:
		print("There is no root-to-leaf path with sum", targetSum)
