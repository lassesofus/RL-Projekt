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

import pandas as pd
'''
# Play one nice, simple and relaxing game of chess:
our_bot = MinimaxAgent(depth=2, stockfish=sf, book=book)
opposite_bot = StockfishAgent(elo_score=1000, stockfish=sf)
env = ChessEnvironment(good_bot=our_bot, bad_bot=opposite_bot)

result = env.play_game()
'''

# Elo score dependant on depth:
depth_range = range(6)
games_per_bot = 1

scores = []
times = []

opponent_scores = [500, 1000, 1500, 2000, 2500, 3000][:3]
no_games = len(opponent_scores)

results = pd.DataFrame(columns=['elo', 'depth', 'time', 'opponent_elo'])

with tqdm(total=len(depth_range)*no_games*games_per_bot) as pbar:
    for i in depth_range:
        game_results = []
        sum_opponent_scores = 0
        for j in range(no_games):
            for k in range(games_per_bot):
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
                sum_opponent_scores += opponent_scores[j]
            elo = get_elo(game_results, opponent_scores[:j+1])
            results = results.append({'elo': elo, 'depth': int(i+1), 'time': avg_movetime, 'opponent_elo': opponent_scores[j]}, ignore_index=True)
            print('\n', results)
results.to_csv('results.csv', index_label='game_number')

# Time for plot
