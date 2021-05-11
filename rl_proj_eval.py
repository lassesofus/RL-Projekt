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

# RECALCULATE ELO TO FIDE
def Ea(Ra, Rb):
    return 1/(1+10**((Ra-Rb)/400))

def Ra_m(Ra, Sa, Ea, K = 40): #https://ratings.fide.com/calculator_rtd.phtml K=40 until 30 games played
    return Ra + K * (Sa - Ea)

def FIDE_elo(df):
    Ra = 1000
    for i in range(len(df)):
        expected = Ea(Ra, df['opponent_elo'][i])
        Sa = df['outcome'][i]
        if Sa == 0:
            Sa = 0.5
        if Sa == -1:
            Sa = 0
        df.iloc[i,5] = Sa
        Ra = Ra_m(Ra, Sa, expected)
        df.iloc[i,0] = Ra
        if df['last_game'][i] == 1:
            Ra = 1000
    return df


# READ DATA
chessdata1 = pd.read_csv("data_results/results_plain.csv", index_col='game_number')
chessdata2 = pd.read_csv("data_results/results_book.csv", index_col='game_number')
chessdata3 = pd.read_csv("data_results/results_sf.csv", index_col='game_number')
chessdata4 = pd.read_csv("data_results/results_both.csv", index_col='game_number')

# RECALC AND MAKE LISTS:
chessdata = [FIDE_elo(chessdata1), FIDE_elo(chessdata2), FIDE_elo(chessdata3), FIDE_elo(chessdata4)]
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
       
    fig = plt.figure(figsize=(8,8))
    #fig.suptitle('Performance of the Chessbot ', fontsize=16)
    ax1 = fig.add_subplot(221)
       
    color = 'steelblue'
    ax1.set_xlabel('Depth')
    ax1.set_ylabel('FIDE Elo-Rate')
    ax1.set_ylim(bottom = 100, top = 1130)
    ax1.set_yticks(np.linspace(150, 1100, 11))
    ax1.tick_params(axis='y')
       
    
    boxplot_plot = pd.concat(dataframes)
    boxplot_plot['Bot'] = 120*[names[0]]+120*[names[1]]+120*[names[2]] + 120*[names[3]]
    ax2 = fig.add_subplot(222)
    sns.lineplot(ax = ax2, x='depth', y="time", hue="Bot", data=boxplot_plot, alpha = 0.7, palette=colors)
    ax2.set_xlabel('Depth')
    ax2.set_ylabel('Avg. time per move (s)')
    ax2.tick_params(axis='y')
    ax2.set_xticks(range(1, len(dataframes)+1))
    ax2.get_legend().remove()
    
    ax3 = fig.add_subplot(223)
    ax3.set_xlabel('Depth')
    ax3.set_ylabel('Avg. Outcome')
    ax3.set_ylim(0, 0.7)
    ax3.axhline(y= 0.5, c='black', ls = '--', alpha = 0.7)
    
       
    boxplot_plot['Interval'] = (10*['100-1000']+10*['1100-2000']+10*['2100-3000'])*4*4
    ax4 = fig.add_subplot(224)
    sns.lineplot(ax = ax4, x='Interval', y="outcome", hue="Bot", data=boxplot_plot, palette=colors, err_style=None)
    ax4.set_xlabel('Intervals of Opponent Elo-rating')
    ax4.set_ylabel('Avg. Outcome')
    ax4.set_yticks(np.linspace(0, 0.6, 7))
    ax4.set_ylim(bottom = -0.05, top = 0.65)
    ax4.axhline(y=0.5, c='black', ls = '--', alpha = 0.7, label = "Center of Win/Loss rate")
    ax4.get_legend().remove()

    
    
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
#        if index == 1: # To solve to bars on top of each others
#            ax2.plot(x_values,plotdata['time'], ls = '--', color = colors[index], alpha = 0.7, lw = 3, label = names[index])
        ax3.bar([float(i)+x_offset for i in x_values], plotdata['outcome'], width=bar_width * single_width, label = names[index], color = colors[index], alpha = 0.7)       
        
    
    lines, labels = fig.axes[-1].get_legend_handles_labels()
    fig.legend(lines, labels, bbox_to_anchor=(0.5, 0), loc = 'lower center', ncol = 5)
    # Plot the whole molevit                right  up   right 
    plt.tight_layout()
    fig.subplots_adjust(bottom=0.12)
    plt.savefig("Results.pdf")
    plt.show()
    

# Runcode: 
process_results_single(chessdata, namesdata)

print('The code ran without incidents')
