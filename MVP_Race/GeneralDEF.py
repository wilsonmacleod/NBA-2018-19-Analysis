import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('dark')

df = pd.read_csv(r'C:\Users\wilso\Desktop\NBA_Analysis\Player-PerGame.csv',index_col=0)
df = df[df['MP']>10]
df['harden'] = df.Player == 'James Harden'
harden = df[df.harden==True]
df['giannis'] = df.Player == 'Giannis Antetokounmpo'
giannis = df[df.giannis==True]
league_players = df[df.harden==False]

fig, axes = plt.subplots(nrows=1, ncols=3, dpi=150)
axes[0].scatter(league_players.MP, league_players.DRB ,label='League', alpha = .8)
axes[0].scatter(harden.MP, harden.DRB, c=sns.xkcd_palette(['light red']), label='Harden')
axes[0].scatter(giannis.MP, giannis.DRB, c=sns.xkcd_palette(['dull green']), label='Giannis')
axes[0].set_title('Defensive Boards')
axes[0].set_xlabel('Minutes Per Game')
axes[0].set_ylabel('Defensive Rebounds per Game')
axes[0].set_xlim(0,40)
axes[0].set_ylim(0,15)
axes[0].grid()
axes[1].scatter(league_players.MP, league_players.STL, label='League', alpha = .8)
axes[1].scatter(harden.MP, harden.STL, c=sns.xkcd_palette(['light red']), label='Harden')
axes[1].scatter(giannis.MP, giannis.STL, c=sns.xkcd_palette(['dull green']), label='Giannis')
axes[1].set_title('Steals')
axes[1].set_xlabel('Minutes Per Game')
axes[1].set_ylabel('Steals per Game')
axes[1].set_xlim(0,40)
axes[1].set_ylim(0,4)
axes[1].grid()
axes[2].scatter(league_players.MP, league_players.BLK, label='League', alpha = .8)
axes[2].scatter(harden.MP, harden.BLK, c=sns.xkcd_palette(['light red']), label='Harden')
axes[2].scatter(giannis.MP, giannis.BLK, c=sns.xkcd_palette(['dull green']), label='Giannis')
axes[2].set_title('Blocks')
axes[2].set_xlabel('Minutes Per Game')
axes[2].set_ylabel('Blocks Per Game')
axes[2].set_xlim(0,40)
axes[2].set_ylim(0,4)
axes[2].grid()
fig.tight_layout()

plt.savefig(fname=r'C:\Users\wilso\Desktop\NBA_Analysis\MVP_Race\figs\generalDEF')