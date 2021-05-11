
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
sf = Stockfish(path + "stockfish_13_win_x64.exe")
book = path + "the-generated-opening-book.bin"

import pandas as pd

# Elo score dependant on depth:
depth = 1
no_games = 0

results = pd.DataFrame(columns=['depth', 'time', 'games', 'moves'])

win = False
while win == False:
	our_bot = MinimaxAgent(depth=depth, stockfish=None, book=None)  # stockfish = sf or/and book = book
	opposite_bot = StockfishAgent(elo_score=3000, stockfish=sf)
	env = ChessEnvironment(good_bot=our_bot, bad_bot=opposite_bot)
	# print('Game', j+1, ' Depth: ',i+1 )
	game, avg_movetime, moves = env.play_game()
	no_games += 1
	if game == '1-0':
		print(moves)
		results = results.append({'depth': depth, 'time': avg_movetime, 'games': no_games,'moves': moves}, ignore_index = True)
		win = True
	#if no_games == 10:
		#results = results.append({'depth': depth, 'time': avg_movetime, 'games': no_games, 'moves': moves}, ignore_index = True)
		#win = True

print('\n', results)
#results.to_csv('results.csv', index_label='game_number')
