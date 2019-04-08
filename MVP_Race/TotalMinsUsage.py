import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('dark')

df = pd.read_csv(r'C:\Users\wilso\Desktop\NBA_Analysis\MVP_Race\data\Player-Advanced.csv',index_col=0)
df = df[df['MP']>=500]
df['harden'] = df.Player == 'James Harden'
harden = df[df.harden==True]
df['giannis'] = df.Player == 'Giannis Antetokounmpo'
giannis = df[df.giannis==True]
league_players = df[df.harden==False]

plt.figure(dpi=75)
plt.scatter(league_players.MP, league_players.USGPer,label='League>500 MP', alpha = .8)
plt.scatter(harden.MP, harden.USGPer, c=sns.xkcd_palette(['light red']), label='Harden')
plt.scatter(giannis.MP, giannis.USGPer, c=sns.xkcd_palette(['dull green']), label='Giannis')
legend = plt.legend(frameon=True, loc=0)
frame = legend.get_frame()
frame.set_edgecolor('black')
plt.xlim(400, 3200)
plt.ylim(0,45)
plt.title('Total Minutes Played vs. Usage%')
plt.xlabel(' Total Minutes')
plt.ylabel('Usage%')
plt.grid()

plt.savefig(fname=r'C:\Users\wilso\Desktop\NBA_Analysis\MVP_Race\figs\TotalMinsUsage')