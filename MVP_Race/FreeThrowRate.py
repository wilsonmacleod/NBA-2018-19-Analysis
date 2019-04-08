import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('dark')

df = pd.read_csv(r'C:\Users\wilso\Desktop\NBA_Analysis\MVP_Race\data\Player-Advanced.csv',index_col=0)
df = df[df['USGPer']>20.00]
df = df[df['MP']>500]
df['harden'] = df.Player == 'James Harden'
harden = df[df.harden==True]
df['giannis'] = df.Player == 'Giannis Antetokounmpo'
giannis = df[df.giannis==True]
league_players = df[df.harden==False]

plt.figure(dpi=75)
plt.scatter(league_players.FGA, league_players.FTr ,label='League> 20% Usage', alpha = .8)
plt.scatter(harden.FGA, harden.FTr, c=sns.xkcd_palette(['light red']), label='Harden')
plt.scatter(giannis.FGA, giannis.FTr, c=sns.xkcd_palette(['dull green']), label='Giannis')
legend = plt.legend(frameon=True, loc=0)
frame = legend.get_frame()
frame.set_edgecolor('black')
plt.xlim(0, 28)
plt.ylim(0,.8)
plt.title('Field Goal Attempts Per Game vs. Free Throw Rate')
plt.xlabel('FGA Per Game')
plt.ylabel('FT Rate%')
plt.grid()
plt.savefig(fname=r'C:\Users\wilso\Desktop\NBA_Analysis\MVP_Race\figs\FreeThrowRate')
