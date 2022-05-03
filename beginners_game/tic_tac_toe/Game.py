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
        # equivalent
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
        return moves


game = Game()
game.available_move()
