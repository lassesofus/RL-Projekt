# Pychess imports
import random

class RandomAgent():
    def __init__(self):
        pass

    def make_move(self, board):
        move = random.choice([move for move in board.legal_moves])
        return move

