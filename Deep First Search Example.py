class Node:
	value = 0
	left = None
	right = None
	def deep_first_search(node, value_to_find):
		if node is None:
			return False
		if node.value == value_to_find:
			return True
		return deep_first_search(node.left, value_to_find) or deep_first_search(node.right, value_to_find)
