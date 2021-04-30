'''

Important Github repositories:
https://github.com/AnthonyASanchez/PythonChessAi/blob/master/AlphaBetaPruning.py
https://github.com/rfma23/ChessAI/blob/main/chessAI.ipynb
https://python-chess.readthedocs.io/en/latest/

'''

# Pychess Imports:
from tqdm import tqdm

# Import classes:
from chessEnvironment import ChessEnvironment
from minimaxAgent import MinimaxAgent
from getScores import get_elo
from stockfishAgent import StockfishAgent

path = ""

#instantiate stockfish:
from stockfish import Stockfish
sf = Stockfish(path + "stockfish_13_win_x64")
book = path + "the-generated-opening-book.bin"

'''
# Play one nice, simple and relaxing game of chess:
our_bot = MinimaxAgent(depth=2, stockfish=sf, book=book)
opposite_bot = StockfishAgent(elo_score=1000, stockfish=sf)
env = ChessEnvironment(good_bot=our_bot, bad_bot=opposite_bot)

result = env.play_game()
'''

# Elo score dependant on depth:
depth_range = range(3)
no_games = 6
scores = []
times = []

opponent_scores = [500, 1000, 1500, 2000, 2500, 3000]

with tqdm(total=len(depth_range)*no_games) as pbar:
    for i in depth_range:
        game_results = []
        for j in range(no_games):
            our_bot = MinimaxAgent(depth=depth_range[i]+1, stockfish=sf, book=book)
            opposite_bot = StockfishAgent(elo_score=opponent_scores[j], stockfish=sf)
            env = ChessEnvironment(good_bot=our_bot, bad_bot=opposite_bot)

            #print('Game', j+1, ' Depth: ',i+1 )
            game, avg_movetime = env.play_game()
            if game == '0-1':
                game_results.append(-1)
            elif game == '1/2-1/2':
                game_results.append(0)
            else:
                game_results.append(1)
            pbar.update(1)
        elo = get_elo(game_results, opponent_scores)
        scores.append(elo)
        times.append(avg_movetime)
print(scores)
print(times)

# Time for plot
