import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv(r'C:\Users\wilso\Desktop\NBA_Analysis\Russ\data\russ18_19.csv')

sns.set_style('whitegrid')
plt.rcParams.update({'font.size': 11})

#3PA vs. Point Diff Figure
x = sns.jointplot(x=df['Unnamed: 6'], y=df['3PA'], kind='reg', xlim=(-30,30), ylim=(0,15), height = 3, 
                color="#ef6400", marginal_kws={'hist_kws': {'edgecolor': "black"}})
x.ax_joint.set_xlabel('Point Differential', fontweight='bold')
x.ax_joint.set_ylabel('3PA', fontweight='bold')

plt.savefig(fname=r'C:\Users\wilso\Desktop\NBA_Analysis\Russ\figs\3pa_pointdiff')

#AST vs. Point Diff Figure
x = sns.jointplot(x=df['Unnamed: 6'], y=df['AST'], kind='reg', xlim=(-25,30), ylim=(4,22), height = 3, 
                color="#408ded", marginal_kws={'hist_kws': {'edgecolor': "black"}})
x.ax_joint.set_xlabel('Point Differential', fontweight='bold')
x.ax_joint.set_ylabel('ASTs', fontweight='bold')

plt.savefig(fname=r'C:\Users\wilso\Desktop\NBA_Analysis\Russ\figs\ast_pointdiff')
