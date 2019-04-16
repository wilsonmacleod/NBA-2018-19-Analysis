import numpy as np
import pandas as pd

df = pd.read_html(f'https://www.basketball-reference.com/players/w/westbru01/gamelog/2019/')
df1 = pd.DataFrame((df[7]))
df = df1[df1['MP']!= 'Inactive']
df = df[df['Rk']!='Rk']
df.reset_index()
df.to_csv(r"C:\Users\wilso\Desktop\NBA_Analysis\Russ\data\russ18_19.csv", sep=',', encoding='utf-8')
