import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 
import pandas as pd
import matplotlib.gridspec as gridspec

chessdata1 = pd.read_csv("results.csv", index_col='game_number')
chessdata2 = chessdata1.copy()
chessdata3 = chessdata1.copy()
chessdata4 = chessdata1.copy()

chessdata = [chessdata1, chessdata2, chessdata3, chessdata4]

# ['elo' 'depth' 'time' 'opponent_elo' 'outcome' ' last_game']
#def plot_performance(dataframe):

def process_results_single(dataframes): # Set modelconfig to one of the following values: "Basic", "Opening Book", "Stockfish", "Both".

	plotdatalist = []

	for index, chessdata in enumerate(dataframes):
		final_score = chessdata[chessdata['last_game'] == True]
		final_score = list(final_score['elo'])

		means = chessdata.groupby('depth').mean()
		means['elo'] = final_score

		plotdata = means.drop(['opponent_elo','last_game'], axis = 1)

		plotdatalist.append(plotdata)

	x_values = list(plotdata.index)

	colors = ['steelblue', 'red', 'orange', 'green']

	#Configure Seaborn
	sns.set_theme()

	# Fist plot:
	fig = plt.figure(figsize=(12,6))
	fig.suptitle('Measuring performance of the Chessbot', fontsize=16)

	ax1 = fig.add_subplot(131)

	color = 'steelblue'
	ax1.set_xlabel('Depth')
	ax1.set_ylabel('ELO-Rate')
	ax1.set_ylim(bottom = 1100, top = 1300)
	ax1.tick_params(axis='y')

	ax2 = fig.add_subplot(132)

	#color = 'tab:blue'
	ax2.set_xlabel('Depth')
	ax2.set_ylabel('Time (s)')
	ax2.tick_params(axis='y')
	ax2.set_xticks([1,2,3])

	ax3 = fig.add_subplot(133)
	#color = 'tab:blue'
	ax3.set_xlabel('Depth')
	ax3.set_ylabel('Score')
	ax3.set_ylim(-1, 1)
	ax3.axhline(y=0, c='red')

	total_width = 0.8
	n_bars = 4
	bar_width = total_width / n_bars
	single_width=1

	# Loop over plotdata to create multiple columns for each bar.
	for index, plotdata in enumerate(plotdatalist):

		# The offset in x direction of that bar
		x_offset = (index - n_bars / 2) * bar_width + bar_width / 2

        # Draw a bar for every value of that type
		ax1.bar([float(i)+x_offset for i in x_values], plotdata['elo'], width=bar_width * single_width, color=colors[index], alpha = 0.7)
		ax2.plot(x_values,plotdata['time'], color = colors[index], alpha = 0.7, lw = 3)
		ax3.bar([float(i)+x_offset for i in x_values], plotdata['outcome'], width=bar_width * single_width, color = colors[index], alpha = 0.7)

	# Plot the whole molevit
	plt.tight_layout()
	plt.show()

# Runcode: 
process_results_single(chessdata)

print('The code ran without incidents')
