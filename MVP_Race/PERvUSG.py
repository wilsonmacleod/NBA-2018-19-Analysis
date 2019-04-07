import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('dark')

df = pd.read_csv(r'C:\Users\wilso\Desktop\NBA_Analysis\Player-Advanced.csv',index_col=0)

df = df[df['MP']>500]
df['harden'] = df.Player == 'James Harden'
harden = df[df.harden==True]
df['giannis'] = df.Player == 'Giannis Antetokounmpo'
giannis = df[df.giannis==True]
league_players = df[df.harden==False]

plt.figure(dpi=150)
plt.scatter(league_players.USGPer, league_players.PER ,label='League>500 Mins', alpha = .8)
plt.scatter(harden.USGPer, harden.PER, c=sns.xkcd_palette(['light red']), label='Harden')
plt.scatter(giannis.USGPer, giannis.PER, c=sns.xkcd_palette(['dull green']), label='Giannis')
plt.xlim(10, 50)
plt.ylim(0,35)
plt.title('Player Efficiency Rating vs. Usage')
plt.xlabel('Usage%')
plt.ylabel('PER')
legend = plt.legend(frameon=True, loc=4)
frame = legend.get_frame()
frame.set_edgecolor('black')
plt.grid()

plt.savefig(fname=r'C:\Users\wilso\Desktop\NBA_Analysis\MVP_Race\figs\PERvUSG')