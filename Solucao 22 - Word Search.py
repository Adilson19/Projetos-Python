class MySolution:
    board = None

    def solution(self, board, word):
        self.board = board

        # Verificar se a posicao atual eh igual a primeira letra da palavra
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                # Eh a primeira posicao da palavra
                if self.board[x][y] == word[0]:
                    move = (x, y)
                    if self.deep_first_search(move, [move], word, 0):
                        return True
        return False
    def deep_first_search(self, current_move, visited_paths, expected_word, word_index):
        # Verificar se a posicao atual eh igual a letra da palavra
        if word_index + 1 >= len(expected_word):
            return True

        x, y = current_move
        possible_moves = [(x - 1, y), 
                          (x + 1, y), 
                          (x, y - 1), 
                          (x, y + 1)]

        board_x_size = len(self.board)
        board_y_size = len(self.board[0])

        for move_x, move_y in possible_moves:
            if move_x >= 0 and move_x < board_x_size and move_y >= 0 and move_y < board_y_size:
                if self.board[move_x][move_y] == expected_word[word_index + 1]:
                    if (move_x, move_y) not in visited_paths:
                        next_move = (move_x, move_y)
                        if self.deep_first_search(next_move,
                                                  visited_paths + [next_move],
                                                  expected_word, 
                                                  word_index + 1):
                            return True
            return False

    # move, visited_paths, expected_word, word_index
    #   Deep First Search
