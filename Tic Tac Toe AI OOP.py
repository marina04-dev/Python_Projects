import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(10)]  # Index 0 is ignored
        self.game_running = True

    def insert_letter(self, letter, pos):
        self.board[pos] = letter

    def space_is_free(self, pos):
        return self.board[pos] == ' '

    def print_board(self):
        print('   |   |')
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('   |   |')

    def is_winner(self, le):
        b = self.board
        return ((b[7] == le and b[8] == le and b[9] == le) or
                (b[4] == le and b[5] == le and b[6] == le) or
                (b[1] == le and b[2] == le and b[3] == le) or
                (b[7] == le and b[4] == le and b[1] == le) or
                (b[8] == le and b[5] == le and b[2] == le) or
                (b[9] == le and b[6] == le and b[3] == le) or
                (b[7] == le and b[5] == le and b[3] == le) or
                (b[9] == le and b[5] == le and b[1] == le))

    def is_board_full(self):
        return self.board.count(' ') <= 1  # Ignore index 0

    def select_random(self, li):
        return random.choice(li)

    def player_move(self):
        while True:
            move = input('Please select a position to place an \'X\' (1-9): ')
            try:
                move = int(move)
                if 1 <= move <= 9:
                    if self.space_is_free(move):
                        self.insert_letter('X', move)
                        break
                    else:
                        print('This position is already occupied!')
                else:
                    print('Please type a number within the range!')
            except ValueError:
                print('Please type a number!')

    def comp_move(self):
        possible_moves = [x for x, letter in enumerate(self.board) if letter == ' ' and x != 0]
        move = 0

        for letter in ['O', 'X']:
            for i in possible_moves:
                board_copy = self.board[:]
                board_copy[i] = letter
                if self.is_winner_on_board(board_copy, letter):
                    return i

        corners_open = [i for i in possible_moves if i in [1, 3, 7, 9]]
        if corners_open:
            return self.select_random(corners_open)

        if 5 in possible_moves:
            return 5

        edges_open = [i for i in possible_moves if i in [2, 4, 6, 8]]
        if edges_open:
            return self.select_random(edges_open)

        return move

    def is_winner_on_board(self, board, le):
        return ((board[7] == le and board[8] == le and board[9] == le) or
                (board[4] == le and board[5] == le and board[6] == le) or
                (board[1] == le and board[2] == le and board[3] == le) or
                (board[7] == le and board[4] == le and board[1] == le) or
                (board[8] == le and board[5] == le and board[2] == le) or
                (board[9] == le and board[6] == le and board[3] == le) or
                (board[7] == le and board[5] == le and board[3] == le) or
                (board[9] == le and board[5] == le and board[1] == le))

    def play(self):
        print('Welcome to Tic Tac Toe!')
        print('To win, complete a straight line (Diagonal, Horizontal, Vertical).')
        print('The board positions are 1-9 starting from the top left.')
        self.print_board()

        while not self.is_board_full():
            if not self.is_winner('O'):
                self.player_move()
                self.print_board()
            else:
                print('O wins this time...')
                return

            if not self.is_winner('X'):
                move = self.comp_move()
                if move == 0:
                    print('Game is a tie! No more spaces left to move.')
                    return
                self.insert_letter('O', move)
                print(f'Computer placed an \'O\' in position {move}:')
                self.print_board()
            else:
                print('X wins, good job!')
                return

        print('Game is a tie! No more spaces left to move.')

# Main game loop
while True:
    game = TicTacToe()
    game.play()
    answer = input('Do you want to play again? (Y/N): ')
    if answer.lower() not in ['y', 'yes']:
        break
    print('-----------------------------------')
