import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('dark')

df = pd.read_csv(r'C:\Users\wilso\Desktop\NBA_Analysis\Player-PerGame.csv',index_col=0)
df = df[df['USGPer']>20.00]
df = df[df['MP']>10]
df['harden'] = df.Player == 'James Harden'
harden = df[df.harden==True]
df['giannis'] = df.Player == 'Giannis Antetokounmpo'
giannis = df[df.giannis==True]
league_players = df[df.harden==False]

plt.figure(dpi=150)
plt.scatter(league_players.TOV, league_players.AST ,label='League>20% USG', alpha = .8)
plt.scatter(harden.TOV, harden.AST, c=sns.xkcd_palette(['light red']), label='Harden')
plt.scatter(giannis.TOV, giannis.AST, c=sns.xkcd_palette(['dull green']), label='Giannis')
plt.xlim(0, 6)
plt.ylim(0,12)
plt.title('Assist vs. Turnover')
plt.xlabel('Turnovers Per Game')
plt.ylabel('Assists Per Game')
legend = plt.legend(frameon=True, loc=0)
frame = legend.get_frame()
frame.set_edgecolor('black')
plt.grid()

plt.savefig(fname=r'C:\Users\wilso\Desktop\NBA_Analysis\MVP_Race\figs\ASTvTOV')