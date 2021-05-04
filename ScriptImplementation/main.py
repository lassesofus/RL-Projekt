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
sf = Stockfish(path + "stockfish_13_linux_x64")
book = path + "the-generated-opening-book.bin"

import pandas as pd
import numpy as np
'''
# Play one nice, simple and relaxing game of chess:
our_bot = MinimaxAgent(depth=2, stockfish=sf, book=book)
opposite_bot = StockfishAgent(elo_score=1000, stockfish=sf)
env = ChessEnvironment(good_bot=our_bot, bad_bot=opposite_bot)

result = env.play_game()
'''

# Elo score dependant on depth:
depth_range = range(4)

scores = []
times = []

opponent_scores = np.linspace(100, 3000, 30)
no_games = len(opponent_scores)

results = pd.DataFrame(columns=['elo', 'depth', 'time', 'opponent_elo', 'outcome', 'last_game'])

with tqdm(total=len(depth_range)*no_games) as pbar:
	for i in depth_range:
		game_results = []
		sum_opponent_scores = 0
		last_game = False
		for opp_elo in opponent_scores:
			our_bot = MinimaxAgent(depth=depth_range[i]+1, stockfish=None, book=None) # stockfish = sf or/and book = book
			opposite_bot = StockfishAgent(elo_score=opp_elo, stockfish=sf)
			env = ChessEnvironment(good_bot=our_bot, bad_bot=opposite_bot)
			#print('Game', j+1, ' Depth: ',i+1 )
			game, avg_movetime = env.play_game()
			if game == '0-1':
				cur_outcome = -1
			if game == '1/2-1/2':
				cur_outcome = 0
			if game == '1-0':
				cur_outcome = 1
			game_results.append(cur_outcome)
			pbar.update(1)
			sum_opponent_scores += opp_elo
			elo = get_elo(game_results, sum_opponent_scores)
			if opp_elo == opponent_scores[-1]:
				last_game = True
			results = results.append({'elo': elo, 'depth': int(i+1), 'time': avg_movetime, 'opponent_elo': opp_elo, 'outcome': cur_outcome, 'last_game': last_game}, ignore_index=True)
			print('\n', results)
results.to_csv('results.csv', index_label='game_number')

# Time for plot
