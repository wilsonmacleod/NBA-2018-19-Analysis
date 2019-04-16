import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams.update({'font.size': 12})
df = pd.read_csv(r'C:\Users\wilso\Desktop\NBA_Analysis\Russ\data\russ18_19.csv')

conditions = [(df['PTS']>=10) & (df['AST']>=10) & (df['TRB']>=10)] #find and mark triple doubles
choices = [1]
df['tripdub'] = np.select(conditions, choices, default=0) 

df['td_sum'] = df['tripdub'].cumsum() #cummulative number triple doubles
df['td_perc'] = ((df['td_sum']/df['G'])*100) #triple double $ per game

df['cum_fg'] = (df['FG'].cumsum()/df['FGA'].cumsum())*100 #fg% per game

data1 = df['td_perc'].as_matrix(columns=None) #figure
data2 = df['cum_fg'].as_matrix(columns=None)

fig, ax1 = plt.subplots(dpi=100, figsize=(8,4))

color = 'tab:blue'
ax1.set_xlabel('Games Played')
ax1.set_ylabel('% of Triple Double Games', color=color)
ax1.bar(df['G'], data1, color=color, label='Triple Double%')
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_ylim(0,55)
ax1.set_xlim(1,73.7)

ax2 = ax1.twinx()
color = 'tab:orange'
ax2.set_ylabel('Season FG% Per Game', color=color) 
ax2.plot(df['G'], data2, color=color, linewidth = 2, label='Season FG%')
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylim(0,55)
plt.grid()

lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc=4, frameon=True, shadow=True)

plt.savefig(fname=r'C:\Users\wilso\Desktop\NBA_Analysis\Russ\figs\tripledoubles_fg')