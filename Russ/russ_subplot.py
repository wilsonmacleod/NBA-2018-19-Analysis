import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

#AST and 3PA subplots
df = pd.read_csv(r'C:\Users\wilso\Desktop\NBA_Analysis\MVP_Race\data\Player-PerGame.csv',index_col=0)
df = df[df['MP']>15]
df['rw'] = df.Player == 'Russell Westbrook'
rw = df[df.rw==True]
league_players = df[df.rw==False]
players_2 = league_players[league_players['ThreePA']>=5]

fig, axes = plt.subplots(nrows=1, ncols=2, dpi=100)
plt.rcParams.update({'font.size': 11})

axes[0].scatter(league_players.MP, league_players.AST, c=sns.xkcd_palette(['black']), label='League', alpha = .8)
axes[0].scatter(rw.MP, rw.AST, c=sns.xkcd_palette(['sky blue']), label='Westbrook')
axes[0].set_title('Leads the League in AST')
axes[0].set_xlabel('Minutes Played')
axes[0].set_ylabel('AST Per Game')
axes[0].legend(loc=2,frameon=True)
axes[0].set_xlim(15,40)
axes[1].set_ylim(2,11)
axes[0].grid()

axes[1].scatter(league_players.ThreePA, league_players.ThreePPer, c=sns.xkcd_palette(['black']), alpha = .8)
axes[1].scatter(rw.ThreePA, rw.ThreePPer, c=sns.xkcd_palette(['sky blue']))
axes[1].set_title('Poor Volume 3-Point Shooter')
axes[1].set_xlabel('3PA')
axes[1].set_ylabel('3-Point%')
axes[1].set_xlim(1,14)
axes[1].set_ylim(0.1,.6)
axes[1].grid()
fig.tight_layout()

plt.savefig(fname=r'C:\Users\wilso\Desktop\NBA_Analysis\Russ\figs\russ_subplot')