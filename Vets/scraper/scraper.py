import numpy as np
import pandas as pd

years = [str(y) for y in range(2000,2020)]
dflist = []

for each in years:
    print(each)
    df = pd.read_html(f'https://www.basketball-reference.com/leagues/NBA_{each}_per_poss.html')
    df1 = pd.DataFrame((df[0]))
    dflist.append(df1)

dfs = pd.concat(dflist, join = 'outer', sort=True)
dfs.to_csv(r"C:\Users\wilso\Desktop\NBA_Analysis\Vets\data\advanced00-19.csv", sep=',', encoding='utf-8')