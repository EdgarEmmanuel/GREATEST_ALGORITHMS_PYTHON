import math
import random

class Player:
    def __init__(self, letter):
        # letter x or o
        self.letter = letter

    def get_move(self, game):
        pass


class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_move())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9)')
            try:
                value = int(square)
                if value in game.available_move():
                    val = value
                    valid_square = True
                else:
                    raise ValueError
            except Exception as e:
                print("Invalid Square Try Again.")
        return val