"""
Created on Fri Jan  8 23:26:31 2021

@author: Ankita Dasgupta

Binary Search Tree
"""

class node:
	def __init__(self, value = None):
		self.value = value
		self.left = None 
		self.right = None 

class bst():
	def __init__(self):
		self.root = None 

	def insert(self, value):
		if self.root == None:
			self.root = node(value)
		else:
			self._insert(value, self.root)

	def _insert(self, value, cur_node):
		if value < cur_node.value:
			if cur_node.left == None:
				cur_node.left = node(value)
			else:
				self._insert(value, cur_node.left)
		elif value > cur_node.value: 
			if cur_node.right == None:
				cur_node.right = node(value)
			else:
				self._insert(value, cur_node.right)
		else:
			print("Value already in tree ")

	def print_tree(self):
		if self.root != None:
			self._print_tree(self.root)

	def _print_tree(self, cur_node):
		if cur_node != None:
			self._print_tree(cur_node.left) 
			print(cur_node.value) 
			self._print_tree(cur_node.right)

	def height(self):
		if self.root != None:
			return self._height(self.root, 0)
		else:
			return 0

	def _height(self, cur_node, cur_height):
		if cur_node == None:
			return cur_height
		left_height = self._height(cur_node.left, cur_height+1)
		right_height = self._height(cur_node.right, cur_height+1) 
		return max(left_height,right_height)

	def search(self,  value):
		if self.root != None:
			return self._search(value, self.root)
		else:
			return False

	def _search(self, value, cur_node):
		if value == cur_node.value:
			return True
		elif value < cur_node.value and cur_node.left != None:
			return self._search(value, cur_node.left)
		elif value > cur_node.value and cur_node.right != None:
			return self._search(value, cur_node.right)
		return False

def fill(tree, num = 100, max_i = 1000):
	from random import randint 
	for i in range(num):
		cur_elem = randint(0,max_i)
		tree.insert(cur_elem)
	return tree

tree = bst()
tree = fill(tree)
tree.print_tree()
print("\n",tree.height())