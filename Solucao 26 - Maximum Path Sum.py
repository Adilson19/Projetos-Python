#                   Arvores binarias: Maximum Path Sum
# 1 - Somar todos os nos a esquerda e a direita
# 2 - Guardar maior valor ate o  momento (esq. + dir. + valor atual)
# 3 - Retornar maior valor (soma a esquerda ou direita) + valor do no atual
# Usamos o Deep First Search

class Solution:
    result = float("-inf")

    def run(self, root):
        self.dfs(root)
        return self.result

    def dfs(self, node):
        if node is None:
            return 0
        #   Somar todos os valores a esquerda
        left_sum = self.dfs(node.left)
        #   Somar todos os valores a direita
        right_sum = self.dfs(node.right)
        #   Se soma esquerda ou direita < 0 entao soma_esq ou direita = 0
        if left_sum < 0:
            left_sum = 0
        right_sum = self.dfs(node.right)
        if right_sum < 0:
            right_sum = 0
        #   Guardar resultado = max(resultado, soma esquerda + soma direita + valor no atual)
        self.result = max(self.result, left_sum + right_sum + node.value)
        #   max(soma esquerda, soma direita) + valor no atual
        return max(left_sum, right_sum) + node.value