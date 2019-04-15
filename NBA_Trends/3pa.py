import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_csv(r'C:\Users\wilso\Desktop\NBA_Analysis\NBA_Trends\data\team_pg09vs19.csv') #fig one

points = df.groupby('year')['PTS'].mean()
threes = df.groupby('year')['3PA'].mean()

df1 = pd.DataFrame(points).reset_index()
df2 = pd.DataFrame(threes).reset_index()

df = df1.join(df2.set_index('year'), on='year')

tres = df['3PA']
pts = df['PTS']

data1 = tres.as_matrix(columns=None)
data2 = pts.as_matrix(columns=None)

fig, ax1 = plt.subplots(dpi=75)

sns.set_style('whitegrid')

color = 'tab:blue'
ax1.set_xlabel('Year of Season')
ax1.set_ylabel('3PA per game', color=color)
ax1.plot(df['year'], data1, color=color, linewidth = 3)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Points Per Game', color=color) 
ax2.plot(df['year'], data2, color=color, linestyle = '--')
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout() 
plt.savefig(fname=r'C:\Users\wilso\Desktop\NBA_Analysis\NBA_Trends\figs\3PAvPTS')

df = pd.read_csv(r'C:\Users\wilso\Desktop\NBA_Analysis\NBA_Trends\data\team_pg09vs19.csv') #fig two
df1 = pd.read_csv(r'C:\Users\wilso\Desktop\NBA_Analysis\NBA_Trends\data\standings.csv')

df1 = df1[df1['year']>2008]
df['year'] = df['year'].astype(int)
df1['year'] = df1['year'].astype(int)
final_df = pd.merge(df,df1,on=['year','Team'])

df = df.groupby(['year','Rk'])['3PA'].mean()
df1 = pd.DataFrame(df).reset_index()

conditions = [(df1['year']>=2005) & (df1['year']<2011),(df1['year']>=2011) & (df1['year']<2014), 
              (df1['year']>=2014) & (df1['year']<2016), (df1['year']>=2016) & (df1['year']<2020)]
choices = ["2008-2010","2011-2013","2014-2016","2017-2019"]
df1['Range'] = np.select(conditions, choices, default="NA")

g = sns.lmplot(x="Rk", y="3PA", x_bins=5, hue="Range", truncate=True, height=4, data=df1)
g.set(xlim=(30,1))
g.set(ylabel="3PA",xlabel="Finishing Positions")
plt.savefig(fname=r'C:\Users\wilso\Desktop\NBA_Analysis\NBA_Trends\figs\3PAvRk')