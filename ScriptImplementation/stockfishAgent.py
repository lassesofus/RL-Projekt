# Pychess imports
import chess
import chess.svg
import chess.polyglot


class StockfishAgent():
    def __init__(self, elo_score = 1000, stockfish = None):
        '''
        :param stockfish: Stockfish object
        '''
        self.stockfish = stockfish
        self.elo_score = elo_score

    def make_move(self, board):
        self.stockfish.set_elo_rating(self.elo_score)
        self.stockfish.set_fen_position(board.fen())
        move = self.stockfish.get_best_move()
        move = chess.Move.from_uci(str(move))
        return move
