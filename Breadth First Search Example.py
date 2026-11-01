class Node:
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
