import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('dark')

df = pd.read_csv(r'C:\Users\wilso\Desktop\NBA_Analysis\MVP_Race\data\Player-PerGame.csv',index_col=0)
df['harden'] = df.Player == 'James Harden'
harden = df[df.harden==True]
df['giannis'] = df.Player == 'Giannis Antetokounmpo'
giannis = df[df.giannis==True]
league_players = df[df.harden==False]

plt.figure(dpi=150)
plt.scatter(league_players.TSPer, league_players.PTS, c=sns.xkcd_palette(['windows blue']), label='League', alpha = .8)
plt.scatter(harden.TSPer, harden.PTS, c=sns.xkcd_palette(['light red']), label='Harden')
plt.scatter(giannis.TSPer, giannis.PTS, c=sns.xkcd_palette(['dull green']), label='Giannis')
legend = plt.legend(frameon=True, loc=0)
frame = legend.get_frame()
frame.set_edgecolor('black')
plt.xlim(0.00,1.0)
plt.ylim(0, 40)
plt.title('Scoring vs TS%')
plt.xlabel('True Shooting Percentage')
plt.ylabel('Points Per Game')
plt.grid()
plt.savefig(fname=r'C:\Users\wilso\Desktop\NBA_Analysis\MVP_Race\figs\ScoringTS')
