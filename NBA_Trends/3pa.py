import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_csv(r'C:\Users\wilso\Desktop\NBA_Analysis\NBA_Trends\data\09vs19.csv')
df = df[df['G']>40] #remove players less than 40 games played
df = df[df['MP']>20]

pd.to_numeric(df['3PA']) #conver to numeric values
pd.to_numeric(df['Year'])

df['Position'] = df['Pos'].apply(lambda title: title.split('-')[0])#merge various hybrid roles into traditional 5

avrge = df.groupby(['Position', 'Year'])['3PA'].mean() 
df = pd.DataFrame(avrge).reset_index()

conditions = [(df['Year']==2009) | (df['Year']==2010) | (df['Year']==2011) | (df['Year']==2012) 
            | (df['Year']==2013) | (df['Year']==2014)]
choices = ["2009-14"]
df['boo'] = np.select(conditions, choices, default="2015-19") #create our two groups of years

sns.set(style='whitegrid') #fig1
plt.figure(figsize=(7,5))
order_rank = ['PG', 'SG', 'SF', 'PF', 'C']
ax = sns.boxenplot(x="Position", y="3PA", hue = 'boo',
              color="r", order=order_rank,
              scale="linear", saturation=100, palette='magma', data=df)
ax.legend(loc="lower left", frameon=True, fontsize = 10)
ax.set(ylabel="Avg 3PA Per Game", xlabel="Position")
plt.savefig(fname=r'C:\Users\wilso\Desktop\NBA_Analysis\NBA_Trends\figs\3PA-boxen')

sns.set(style='whitegrid') #fig2
plt.figure(figsize=(7,5))
order_rank = ['PG', 'SG', 'SF', 'PF', 'C']
ax = sns.relplot(x='Year', y="3PA",
            hue="Position", hue_order=order_rank,
            height=5, aspect=.75, facet_kws=dict(sharex=False),
            kind="line", legend="full", data=df)
ax.set(ylabel="Avg 3PA Per Game", xlabel="Position")
plt.savefig(fname=r'C:\Users\wilso\Desktop\NBA_Analysis\NBA_Trends\figs\3PA-line')