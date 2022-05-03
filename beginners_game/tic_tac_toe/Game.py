class Game:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        # from 0 to 2
        # from 3 to 5
        # from 6 to 8
        rows = [self.board[i*3:(i+1)*3] for i in range(3)]
        for row in rows:


game = Game()
game.print_board()