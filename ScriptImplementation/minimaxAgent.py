# Pychess imports
import chess
import chess.svg
import chess.polyglot
import numpy as np

from staticBoardEvaluation import StaticBoardEvaluation
from alphaBetaSearch import alphabeta_search

class MinimaxAgent():
    def __init__(self, depth=2, stockfish = None, book = None):

        '''
        :param depth: Integer, a depth for the alpha-beta search tree
        :param stockfish: Stockfish object
        :param book: String, path to the opening book
        '''

        self.depth = depth
        self.book = book
        self.stockfish = stockfish
        #if self.stockfish is not None:
            #self.stockfish_eval = True


    def evaluate_board(self, board):
        if self.stockfish is not None:
            self.stockfish.set_elo_rating(3500)
            self.stockfish.set_fen_position(board.fen())
            result = self.stockfish.get_evaluation()
            if result['type'] == 'mate':
                total_score = 10000 + result['value']
            else:
                total_score = result['value']

        else:
            """Assigns a score to the board according to several metrics:
                - the value of the piece
                - the position of the piece
    
            Parameters
            ----------
            board : chess.Board
            """
            total_score = 0

            piece_value = StaticBoardEvaluation.piece_value
            position_value = StaticBoardEvaluation.position_value


            if board.is_checkmate():
                if board.turn == chess.WHITE:
                    return -10000
                else:
                    return 10000

            for square in chess.SQUARES:
                piece = board.piece_at(square)
                if piece is not None:
                    x = chess.square_file(square)  # Letter - column
                    y = chess.square_rank(square)  # Number - row

                    value = piece_value[piece.piece_type] + \
                            position_value[piece.piece_type][piece.color][y][x]

                    # invert sign if black
                    if piece.color == chess.BLACK: value = - value  # Invert score - white maximise, black minimise

                    total_score += value

        return total_score

    def make_move(self, board):
        turn = board.turn
        try:
            if self.book is None:
                # print('Use opening book is deactivated')
                raise ValueError()
            book_move = chess.polyglot.MemoryMappedReader(self.book).weighted_choice(board).move #  Beware: Denne bog risikerer at flyttes
            # print('Used Opening Book')
            return book_move
        except:
            depth = self.depth
            best_move, _ = alphabeta_search(self, board, depth, to_move = turn)
            return best_move




