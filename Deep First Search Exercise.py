#	Exercicio de Um labirinto para achar o valor 99
maze = [...]

#	Funcao para buscar a proxima posicao valida
def find_next_position(position, visited_position):
	return 0, 0

#	Funcao para pegar o valor dentro de uma determinada posicao onde temos os valores X e Y
def item_value(position):
	return maze[position[0]][position[1]]

#	Funcao Principal chamada: deep_first_search
def deep_first_search(position, visited_positions, value_to_find):

	#	Pegar o valor apartir da funcao a cima e comparar se eh realmente que desejamos 
	if item_value(position) == value_to_find:

		#	Se for o valor que estamos procurando ele retorna de imediato o valor True
		return True
	
	#	Pegando a proxima posicao valida, mas deve ser para baixo, direita, cima e esquerda
	next_position = find_next_position(position, visited_positions)

	#	Se encontrarmos uma posicao valida entao ele farah o seguinte:
	if next_position:

		#	Chamamos de forma recursiva a funcao deep_first_search
		return deep_first_search(next_position, visited_positions + [position], value_to_find)