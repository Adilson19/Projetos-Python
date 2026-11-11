#   Criar matriz com valores zerado do mesmo tamanho da nossa matriz recebida
#   Enumerar cada item da matriz
#   Chamar a dfs
#   Chamar somente se nao tiver o numero calculado no nosso count_matrix
#   Retornar o valor do count_matrix na posicao atual
#   Validar movimentacao e chamar ele mesmo se for uma movimentacao valida (para o proximo passo)
#   retornar o valor maioir do count_matrix

def solution(matrix):

    def is_valid_position(pos1, pos2, value):        
        if pos1 >= 0 and pos1 < vertical_size:
            if pos2 >= 0 and pos2 < horizontal_size:
                return value < matrix[pos1][pos2]
    #   Validar movimentacao e chamar ele mesmo se for uma movimentacao valida (para o proximo passo)
    def dfs(pos1, pos2):
        #   Chamar somente se nao tiver o numero calculado no nosso count_matrix
        if count_matrix[pos1][pos2] == 0:
            value = matrix[pos1][pos2]

            max_path = 0
            #   Validar movimentacao e chamar ele mesmo se for uma movimentacao valida (para o proximo passo)
            for next_pos1, next_pos2 in [(pos1 - 1, pos2), (pos1 + 1, pos2), 
                                         (pos1, pos2 - 1), (pos1, pos2 + 1)]:
                #   Validar movimentacao e chamar ele mesmo se for uma movimentacao valida (para o proximo passo)
                if is_valid_position(next_pos1, next_pos2, value):
                    max_path = max(max_path, dfs(next_pos1, next_pos2))
            count_matrix[pos1][pos2] = 1 + max_path

            #   (pos1 - 1, pos2) - cima
            #   (pos1 + 1, pos2) - baixo
            #   (pos1, pos2 - 1) - esquerda
            #   (pos1, pos2 + 1) - direita
        #   Retornar o valor do count_matrix na posicao atual
        return count_matrix[pos1][pos2]
    
    result = 0
    if matrix and matrix[0]:            
        #   Criar matriz com valores zerado do mesmo tamanho da nossa matriz recebida
        vertical_size, horizontal_size = len(matrix), len(matrix[0])
        count_matrix = [[0] * horizontal_size for i in range(vertical_size)]
        #   Enumerar cada item da matriz
        for pos1 in range(vertical_size):
            for pos2 in range(horizontal_size):
                result = max(result, dfs(pos1, pos2))

    return result