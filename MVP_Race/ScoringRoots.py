import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('dark')

df = pd.read_csv(r'C:\Users\wilso\Desktop\NBA_Analysis\MVP_Race\data\Player-PerGame.csv',index_col=0)
df = df[df['TwoPA']>2]
df['harden'] = df.Player == 'James Harden'
harden = df[df.harden==True]
df['giannis'] = df.Player == 'Giannis Antetokounmpo'
giannis = df[df.giannis==True]
league_players = df[df.harden==False]

fig, axes = plt.subplots(nrows=1, ncols=3, dpi=100)
axes[0].scatter(league_players.TwoPA, league_players.TwoP ,label='League', alpha = .8)
axes[0].scatter(harden.TwoPA, harden.TwoP, c=sns.xkcd_palette(['light red']), label='Harden')
axes[0].scatter(giannis.TwoPA, giannis.TwoP, c=sns.xkcd_palette(['dull green']), label='Giannis')
axes[0].set_title('2-Point')
axes[0].set_xlabel('2-Point FGA')
axes[0].set_ylabel('2-Point Makes')
axes[0].set_xlim(0,20)
axes[0].set_ylim(0,10)
axes[0].grid()
axes[1].scatter(league_players.ThreePA, league_players.ThreeP, label='League', alpha = .8)
axes[1].scatter(harden.ThreePA, harden.ThreeP, c=sns.xkcd_palette(['light red']), label='Harden')
axes[1].scatter(giannis.ThreePA, giannis.ThreeP, c=sns.xkcd_palette(['dull green']), label='Giannis')
axes[1].set_title('3-Point')
axes[1].set_xlabel('3-Point FGA')
axes[1].set_ylabel('3-Point Makes')
axes[1].set_xlim(0,20)
axes[1].set_ylim(0,10)
axes[1].grid()
axes[2].scatter(league_players.FTA, league_players.FT, label='League', alpha = .8)
axes[2].scatter(harden.FTA, harden.FT, c=sns.xkcd_palette(['light red']), label='Harden')
axes[2].scatter(giannis.FTA, giannis.FT, c=sns.xkcd_palette(['dull green']), label='Giannis')
axes[2].set_title('Free Throws')
axes[2].set_xlabel('FT Attempts')
axes[2].set_ylabel('FT Makes')
axes[2].set_xlim(0,25)
axes[2].set_ylim(0,10)
axes[2].grid()
fig.tight_layout()
plt.savefig(fname=r'C:\Users\wilso\Desktop\NBA_Analysis\MVP_Race\figs\ScoringRoots')
