Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Node:
	value = 0
	left = None
	right = None
	def breadth_first_search(root, value_to_find):
		if root:
			queue = [root]
			while queue:
				node = queue.pop(0)
				# Checa condicao se eh o no que esperamos
				if node.value == value_to_find:
					return True
				# Vamos analisar os nos filhos
				if node.left:
					queue.append(node.left)
				if node.right:
					queue.append(node.right)
