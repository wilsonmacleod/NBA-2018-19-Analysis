import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('dark')

df = pd.read_csv(r'C:\Users\wilso\Desktop\data\Player-Advanced.csv',index_col=0)
df = df[df['MP']>=500]
df['harden'] = df.Player == 'James Harden'
harden = df[df.harden==True]
df['giannis'] = df.Player == 'Giannis Antetokounmpo'
giannis = df[df.giannis==True]
league_players = df[df.harden==False]

plt.figure(dpi=75)
plt.scatter(league_players.PTS, league_players.TSPer, c=sns.xkcd_palette(['windows blue']), label='League>20PPG', alpha = .8)
plt.scatter(harden.PTS, harden.TSPer, c=sns.xkcd_palette(['light red']), label='Harden')
plt.scatter(giannis.PTS, giannis.TSPer, c=sns.xkcd_palette(['dull green']), label='Giannis')
legend = plt.legend(frameon=True, loc=0)
frame = legend.get_frame()
frame.set_edgecolor('black')
plt.xlim(20, 40)
plt.ylim(.4, 1.0)
plt.title('Scoring vs TS%')
plt.xlabel('Points Per Game')
plt.ylabel('True Shooting Percentage')
plt.grid()
plt.savefig(fname=r'C:\Users\wilso\Desktop\NBA_Analysis\MVP_Race\figs\ScoringTS')
