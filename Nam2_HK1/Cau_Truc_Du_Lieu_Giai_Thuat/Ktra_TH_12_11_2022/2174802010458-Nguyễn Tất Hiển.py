# Python3 program to implement
# the above approach
from collections import deque

# A Binary Tree Node
class node:
	
	def __init__(self):
		
		# Left Child
		self.left = None

		self.data = 0

		# Right Child
		self.right = None

# Function to perform level order traversal
# count levels with all 1s grouped together
def countLevels(root):

	if (root == None):
		return 0

	Count = 0

	# Create an empty queue for
	# level order traversal
	q = deque()

	# Stores front element of the queue
	curr = node()

	# Enqueue root and None node
	q.append(root)

	# Stores Nodes of
	# Current Level
	while q:
		n = len(q)
		flag0 = 0
		flag1 = 0
		flag2 = 0

		while (n):

			# Stores first node of
			# the current level
			curr = q[0]
			q.popleft()

			if (curr):

				# If left child exists
				if (curr.left):

					# Push into the Queue
					q.append(curr.left)

				# If right child exists
				if (curr.right):

					# Push into the Queue
					q.append(curr.right)

				if (curr.data == 1):

					# If current node is the first
					# node with value 1
					if (not flag1):
						flag1 = 1

					# If current node has value 1
					# after occurrence of nodes
					# with value 0 following a
					# sequence of nodes with value 1
					if (flag1 and flag0):
						flag2 = 1

				# If current node is the first node
				# with value 0 after a sequence
				# of nodes with value 1
				if (curr.data == 0 and flag1):
					flag0 = 1

			n -= 1

		if (flag1 and not flag2):
			Count += 1

	return Count

# Function to create a Tree Node
def newNode(data):

	temp = node()
	temp.data = data
	temp.left = None
	temp.right = None
	return temp

# Driver Code
if __name__ == "__main__":

	root = newNode(0)
	root.left = newNode(0)
	root.right = newNode(1)
	root.left.left = newNode(0)
	root.left.right = newNode(1)
	root.right.left = newNode(1)
	root.right.right = newNode(0)

	print(countLevels(root))

# This code is contributed by sanjeev2552
