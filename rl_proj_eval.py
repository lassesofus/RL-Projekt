# -*- coding: utf-8 -*-
"""
Created on Thu May  6 23:53:34 2021

@author: Jonas
"""
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 
import pandas as pd
import matplotlib.gridspec as gridspec

chessdata1 = pd.read_csv("data_results/results_plain.csv", index_col='game_number')
chessdata2 = pd.read_csv("data_results/results_book.csv", index_col='game_number')
chessdata3 = pd.read_csv("data_results/results_sf.csv", index_col='game_number')
chessdata4 = pd.read_csv("data_results/results_both.csv", index_col='game_number')

chessdata = [chessdata1, chessdata2, chessdata3, chessdata4]
namesdata = ['Plain', 'Book', 'Stockfish', 'Both']

# ['elo' 'depth' 'time' 'opponent_elo' 'outcome' ' last_game']
#def plot_performance(dataframe):

def process_results_single(dataframes, names): # Set modelconfig to one of the following values: "Basic", "Opening Book", "Stockfish", "Both".
   
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
    fig = plt.figure(figsize=(10,4))
    fig.suptitle('Performance of the Chessbot ', y=1.03, fontsize=16)
    ax1 = fig.add_subplot(131)
       
    color = 'steelblue'
    ax1.set_xlabel('Depth')
    ax1.set_ylabel('ELO-Rate')
    ax1.set_ylim(bottom = 1150, top = 1700)
    ax1.tick_params(axis='y')
       
    ax2 = fig.add_subplot(132)
       
    # color = 'tab:blue'
    ax2.set_xlabel('Depth')
    ax2.set_ylabel('Avg. time per move (s)')
    ax2.tick_params(axis='y')
    ax2.set_xticks(range(1, len(dataframes)+1))
       
    ax3 = fig.add_subplot(133)
       	#color = 'tab:blue'
    ax3.set_xlabel('Depth')
    ax3.set_ylabel('Avg. Outcome')
    ax3.set_ylim(-1, 1)
    ax3.axhline(y=0, c='black')
       
    total_width = 0.8
    n_bars = 4
    bar_width = total_width / n_bars
    single_width=1
   
   	# Loop over plotdata to create multiple columns for each bar.
    for index, plotdata in enumerate(plotdatalist):
        # The offset in x direction of that bar
        x_offset = (index - n_bars / 2) * bar_width + bar_width / 2
    
        # Draw a bar for every value of that type
        ax1.bar([float(i)+x_offset for i in x_values], plotdata['elo'], width=bar_width * single_width, label = names[index], color=colors[index], alpha = 0.7)
        if index == 1: # To solve to bars on top of each others
            ax2.plot(x_values,plotdata['time'], ls = '--', color = colors[index], alpha = 0.7, lw = 3, label = names[index])
        else:
            ax2.plot(x_values,plotdata['time'], color = colors[index], alpha = 0.7, lw = 3, label = names[index])
        print(plotdata['time'])
        ax3.bar([float(i)+x_offset for i in x_values], plotdata['outcome'], width=bar_width * single_width, label = names[index], color = colors[index], alpha = 0.7)
        plt.legend()
    # Plot the whole molevit
    plt.tight_layout()
    plt.savefig("Results.pdf")
    plt.show()

# Runcode: 
process_results_single(chessdata, namesdata)

print('The code ran without incidents')
