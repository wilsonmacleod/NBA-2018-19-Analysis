import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_csv(r'C:\Users\wilso\Desktop\NBA_Analysis\NBA_Trends\data\standings.csv')

team = ['New Jersey Nets', 'Washington Wizards', 'Houston Rockets', 'Cleveland Cavaliers', 'Orlando Magic', 
        'Milwaukee Bucks', 'Toronto Raptors', 'Portland Trail Blazers', 'Chicago Bulls', 'LA Clippers'] 
year = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009] #year of 1 picks
labels = ['NJ', 'WA', 'HOU', 'CLE', 'ORL', 'MIL', 'TOR', 'POR', 'CHI', 'LAC']
counter = 0

for each in team:
    team = df[(df['Team']==f'{each}') & (df['year']>=int(f'{year[counter]}')) & (df['year']<=int(f'{year[counter]}')+5)].reset_index()
    team['years_since'] = team.index
    labels[counter] = team
    counter += 1
df = pd.concat(labels)

final_df = pd.DataFrame()
for team in df['Team'].unique():
    team_stats = df[df['Team']==str(team)]
    year_one = team_stats[team_stats['years_since']==0]['W/L%']
    team_stats['trend'] = (team_stats['W/L%'] - float(year_one))*100
    final_df = final_df.append(team_stats)

sns.set_style('whitegrid')
plt.figure(figsize=(10, 10), dpi=75) #box plot fig
sns.boxplot(final_df['years_since'], final_df['trend'], palette = 'magma', fliersize = 6)
plt.xlabel('Years since obtaining 1st pick')
plt.ylabel('Trend in Win% +/-')
plt.savefig(fname=r'C:\Users\wilso\Desktop\NBA_Analysis\NBA_Trends\figs\theprocess')