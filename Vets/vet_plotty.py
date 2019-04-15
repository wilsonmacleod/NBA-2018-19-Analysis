import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'C:\Users\wilso\Desktop\NBA_Analysis\Vets\data\advanced00-19.csv').reset_index()
df = df[(df['ORtg']>75) & (df['ORtg']<200)] #remove statiscal outliers
df = df[(df['DRtg']>75) & (df['DRtg']<200)] 
df = df[df['Age'] >= 19]
df = df[df['Age'] < 38]

ortg = df.groupby(['Age'])['ORtg'].mean()
ortg = pd.DataFrame(ortg).reset_index()

drtg = df.groupby(['Age'])['DRtg'].mean()
drtg = pd.DataFrame(drtg).reset_index()

data1 = ortg.as_matrix(columns=None) #figure 1
data2 = drtg.as_matrix(columns=None)

fig, ax1 = plt.subplots(dpi=75, figsize=(10,5))

color = 'tab:blue'
ax1.set_xlabel('Age')
ax1.set_ylabel('Offensive Rating', color=color)
ax1.plot(ortg['Age'], data1, color=color, linewidth = 3)
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_ylim(100,106)
ax1.set_xlim(19,37)
ax1.set_title('Off & Def vs. Age')

ax2 = ax1.twinx()
color = 'tab:green'
ax2.set_ylabel('Defensive Rating', color=color) 
ax2.plot(drtg['Age'], data2, color=color, linewidth = 3)
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylim(105,108)
fig.tight_layout() 
plt.savefig(fname=r'C:\Users\wilso\Desktop\NBA_Analysis\Vets\figs\ratings')

df = pd.read_csv(r'C:\Users\wilso\Desktop\NBA_Analysis\Vets\data\advanced00-19.csv').reset_index() #figure 2
df = df[df['MP'] > 1000]
df = df[df['G'] > 30]
df = df[df['Age'] >= 19]
df = df[df['Age'] < 36]

tov = df.groupby('Age')['TOV'].mean()
tov = pd.DataFrame(tov).reset_index()

fouls = df.groupby('Age')['PF'].mean()
fouls = pd.DataFrame(fouls).reset_index()

fig, axes = plt.subplots(nrows=1, ncols=2, dpi=100, figsize=(10,4))
axes[0].plot(tov['Age'], tov['TOV'],label='Turnovers', linewidth = 3)
axes[0].set_xlabel('Age')
axes[0].set_ylabel('TOV per 100 possessions')
axes[0].set_xlim(19,35)
axes[0].set_ylim(2,4)
axes[0].grid()
axes[1].plot(fouls['Age'], fouls['PF'],label='Fouls', linewidth = 3)
axes[1].set_xlabel('Age')
axes[1].set_ylabel('Personal Fouls per 100 possessions')
axes[1].set_xlim(19,35)
axes[1].set_ylim(4,6)
axes[1].grid()
fig.tight_layout()
plt.savefig(fname=r'C:\Users\wilso\Desktop\NBA_Analysis\Vets\figs\to_pf')

sns.set_style('darkgrid')

df = pd.read_csv(r'C:\Users\wilso\Desktop\NBA_Analysis\Vets\data\advanced00-19.csv').reset_index()
df = df[df['MP'] > 500]
df = df[df['G'] > 30]
df = df[df['Age'] >= 18]
df = df[df['Age'] < 37]

fga = df.groupby('Age')['FGA'].mean()
fga = pd.DataFrame(fga).reset_index()

ast = df.groupby('Age')['AST'].mean()
ast = pd.DataFrame(ast).reset_index()

data1 = fga.as_matrix(columns=None)
data2 = ast.as_matrix(columns=None)

fig, ax1 = plt.subplots(dpi=75, figsize=(10,5))

color = 'tab:blue'
ax1.set_xlabel('Age')
ax1.set_ylabel('Field goals Per 100', color=color)
ax1.plot(fga['Age'], data1, color=color, linewidth = 3)
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_ylim(14,18)
ax1.set_xlim(19,35)
ax1.set_title('Players Shoot Less and Assist More As They Get Older')

ax2 = ax1.twinx()
color = 'tab:green'
ax2.set_ylabel('Assists Per 100', color=color) 
ax2.plot(fga['Age'], data2, color=color, linewidth = 3)
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylim(3,6)
fig.tight_layout() 
plt.savefig(fname=r'C:\Users\wilso\Desktop\NBA_Analysis\Vets\figs\pts_ast')