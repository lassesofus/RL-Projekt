import chess
from tkinter import Tk
import gui
from minimaxAgent import MinimaxAgent
from stockfish import Stockfish

sf = Stockfish("stockfish_13_win_x64.exe")
stockfish = sf
depth = 3
book = "the-generated-opening-book.bin"

PentaBot = MinimaxAgent(depth=depth, stockfish = stockfish, book = book)

class Game:
    board = chess.Board()
    print('Chose your color (1 = White, 0 = Black): ')
    player_turns1 = input()
    player_turns = [True if player_turns1 == '1' else False]
    is_player_white = player_turns[-1]

    root = Tk()
    title = "Interactive game against a {} with depth {}.".format(type(PentaBot).__name__, depth)
    if stockfish is not None:
        title = title[:-1]
        title += " and stockfish evaluation."
    if book is not None:
        title = title[:-1]
        title += " and opening book."

    root.title(title)

    def __init__(self):
        self.display = gui.GUI(self.root, self, self.board, self.player_turns)
        self.display.pack(
            side='top', fill='both', expand='true', padx=4, pady=4)

    def start(self):
        if self.player_turns[-1]:
            self.display.label_status["text"] = "You play as white."

            self.root.after(1000, self.player_play)
        else:
            self.display.label_status[
                "text"] = "You play as black. The computer is thinking..."

            self.root.after(1000, self.computer_play)

        self.root.mainloop()

    def player_play(self):
        self.display.label_status["text"] = "Player's turn."
        # wait as long as possible for player's input
        self.root.after(100000000, self.computer_play)

    def computer_play(self):
        chosen_move = PentaBot.make_move(self.board)
        self.board.push(chosen_move)

        self.display.refresh()
        self.display.draw_pieces()

        self.player_turns.append(True)
        if self.board.is_checkmate():
            self.display.label_status["text"] = "Checkmate."
        elif self.board.is_stalemate():
            self.display.label_status["text"] = "It was a draw."
        else:
            self.display.label_status[
                "text"] = "Computer's turn. The computer is thinking..."

            self.root.after(100, self.player_play)


Game().start()