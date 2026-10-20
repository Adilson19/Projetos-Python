Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Node:
	value = 0
	left = None
	right = None
	def deep_first_search(node, value_to_find):
		if node is None:
			return False
		if node.value == value_to_find:
			return True
		return deep_first_search(node.left, value_to_find) or \ deep_first_search(node.right, value_to_find)
	
SyntaxError: unexpected character after line continuation character
>>> 
