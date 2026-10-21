#   A solucao deve estar implementada dentro da funcao abaixo
#   Dica: voce pode criar outras funcoes e classes se quiser mas esta eh a funcao principal que sera usada
'''
Definicoes da classe de arvore binaria
class BinaryTree:
    value = 0
    left = None
    right = None
'''

def solution(root):
    #   Verificando o parametro
    if root:
        queue = [(root, 1)] #    Inicializando o nivel
        while queue:
            node, level = queue.pop(0)  # Pegando o primeiro item da primeira fila 

            #   Verificando se existe algum no filho
            if node.left is None and node.right is None:
                return level
            level += 1
            if node.left:
                queue.append((node.left, level))

            if node.right:
                queue.append((node.right, level))
    return 0

        


#   Identificar qual eh o nivel mais raso aonde nao temos filhos
queue = [9]

queue = [3, 1]
queue = [2, 4, 6, 8]