import chess
import chess.svg
import chess.polyglot
import time

class ChessEnvironment():
    def __init__(self, good_bot = None, bad_bot = None):
        self.good_bot = good_bot
        self.bad_bot = bad_bot

    def play_game(self, init_fen=None):

        # start a game with the default setup
        if init_fen is None: init_fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
        board = chess.Board(fen=init_fen)
        # chess.svg.board(board, size=250)
        states = []
        runtimes = []

        while not board.is_game_over():
            # White move - this is our chess-bot so it is hardcoded with 'self' - needs to use alpha-beta search.
            # First look for opening book moves

            # board.turn = chess.WHITE
            start_time = time.time()
            best_move = self.good_bot.make_move(board)
            runtime = time.time()-start_time
            runtimes.append(runtime)

            ''' 
            THIS IS COSMETIC, ACTIVATE AT A LATER TIME
            if stockfish_eval:
                val = stockfish_evaluation(board=board)
            else:
                val = evaluate_board(board)
            # print(f'White plays: {best_move}  of approx. value: {val}')
            '''
            board.push(best_move)
            states.append(board.fen())
            #print("WHITE MOVE:")
            #print(board)

            if board.is_game_over():
                break

            # Play against you or another MiniMax agent
            # Opponent move
            # board.turn = chess.BLACK

            move = self.bad_bot.make_move(board)
            board.push(move)
            states.append(board.fen())
            #print("BLACK MOVE:")
            #print(board)

            '''
            THIS IS COSMETIC, ACTIVATE AT A LATER TIME
            if stockfish_eval:
                val = stockfish_evaluation(board=board)
            else:
                val = evaluate_board(board)
            # print(f'Black plays: {move}  of approx. value: {val}')
            # print(board , "\n")
            '''

            if board.is_game_over():
                break

        avg_movetime = sum(runtimes)/len(runtimes)
        #print(f'Result:  White {board.result()} Black')
        return board.result(), avg_movetime