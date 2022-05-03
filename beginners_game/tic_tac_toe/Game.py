from Player import HumanPlayer, ComputerPlayer


class Game:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        # from 0 to 2
        # from 3 to 5
        # from 6 to 8
        rows = [self.board[i * 3:(i + 1) * 3] for i in range(3)]
        for row in rows:
            print(" | " + " | ".join(row) + " | ")

    @staticmethod
    def print_board_nums():
        rows_number = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        # ===== the equivalent with for loop =======
        # rows = []
        # for j in range(3):
        #     inter = []
        #     for i in range(j*3, (j+1)*3):
        #         inter.append(str(i))
        #     rows.append(inter)
        # print(rows)
        for row in rows_number:
            print(" | " + " | ".join(row) + " | ")

    def available_move(self):
        moves = [i for (i, spot) in enumerate(self.board) if spot == ' ']
        # ===== the quivalent with for loop
        # moves = []
        # for (i,spot) in enumerate(self.broad):
        #     if spot == ' ':
        #         moves.append(i)
        return moves

    def empty_games(self):
        space = ' '
        return space in self.board

    def num_empty_squares(self):
        space = ''
        return self.board.count(space)

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def checkWinnerByRow(self, square, letter):
        rows = [self.board[i * 3:(i + 1) * 3] for i in range(3)]
        for row in rows:
            if square in row:
                length = len(row)
                num = 0
                for (i, spot) in enumerate(row):
                    if spot == letter:
                        num += 1
                if num == length:
                    return True
                else:
                    return False

    def winner(self, square, letter):
        # check row
        self.checkWinnerByRow(square, letter)

        # check column
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'
    X_PLAYER = 'X'
    O_PLAYER = 'O'

    while game.empty_games():
        square = None
        if letter == X_PLAYER:
            square = x_player.get_move(game)
        if letter == O_PLAYER:
            square = o_player.get_move(game)

        # make the user move
        if game.make_move(square, letter):
            if print_game:
                print(f"{letter} Has done a move to {square}")
                game.print_board()
                print('')

            # check if a user has won the game
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')

            # alternate the user
            letter = O_PLAYER if letter == X_PLAYER else X_PLAYER

        if print_game:
            print("It's a tie")


if __name__ == "__main__":
    x_player = HumanPlayer('X')
    o_player = ComputerPlayer('O')
    tictactoe = Game()
    play(tictactoe, x_player, o_player, print_game=True)
