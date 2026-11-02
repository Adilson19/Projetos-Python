 #  Deep First Search
class Solution:    
    def run(self, root, expected_sum):
        result = []
        if root:
            self.dfs(root, [], 0, expected_sum, result)
        return result

    def dfs(self, node, current_path, current_sum, expected_sum, result):
        if node is None:
            return
        current_sum += node.value
        # ultimos itens da arvore
        node_without_left = node.left is None and node.right is None
        if node_without_left and current_sum == expected_sum:
            result += [current_path + [node.value]]
            return

        self.dfs(node.left, current_path + [node.value], current_sum, expected_sum, result)
        self.dfs(node.right, current_path + [node.value], current_sum, expected_sum, result)
