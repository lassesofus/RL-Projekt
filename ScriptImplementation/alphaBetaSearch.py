import chess
import numpy as np
def alphabeta_search(agent, board, depth, alpha=None, beta=None, to_move=None):
    """Minimax Tree evaluation improved by not considering positions
    that can't affect the outcome.

    Parameters
    ----------
    board : chess.Board
        a chess board with a particular setup (pieces->squares)
    depth : int
        how many moves ahead we want to think
    alpha : int, optional
        highest value in the subtree, by default -np.infty
    beta : int, optional
        lowest value in the subtree, by default np.infty
    to_move : chess.Player, optional
        the player whose turn it is to make a move, by default None
    """
    # depth = self.depth # Make copy so the recursive call works correctly.

    if alpha is None: alpha = -np.infty
    if beta is None: beta = np.infty
    if depth == 0 or board.is_game_over():
        # static eval - end of recursion
        # asyncio.set_event_loop_policy(chess.engine.EventLoopPolicy())
        return board.peek(), agent.evaluate_board(board)

    if to_move == chess.WHITE:  # maximise

        max_val = -np.infty
        best_move = None

        # we should explore each tree branch
        for move in board.legal_moves:

            # simulate the move (explore the branch)
            board.push(move)

            # evaluate it
            _, value = alphabeta_search(agent, board, depth - 1, alpha, beta, to_move=chess.BLACK)

            # if best move seen, update it
            if value > max_val:
                best_move = move
                max_val = value

            # take it back (return to parent)
            board.pop()

            alpha = max(alpha, value)
            # no sense checking other options as the player is not
            # likely to choose this branch under the hypothesis
            # he performs the best move, otherwise if he does he
            # will end in a situation worse for him
            if beta <= alpha: break

        return best_move, max_val


    else:  # black -> minimise

        min_val = np.infty
        best_move = None

        # we should explore the tree
        for move in board.legal_moves:

            # simulate the move (explore the branch)
            board.push(move)

            # evaluate it
            _, value = alphabeta_search(agent, board, depth - 1, alpha, beta, to_move=chess.WHITE)

            # if best move seen, update it
            if value < min_val:
                best_move = move
                min_val = value

            # take it back (return to parent)
            board.pop()

            beta = min(beta, value)
            # no sense checking other options as the player is not
            # likely to choose this branch under the hypothesis
            # he performs the best move, otherwise if he does he
            # will end in a situation worse for him
            if beta <= alpha: break

        return best_move, min_val