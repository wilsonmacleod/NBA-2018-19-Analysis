import numpy as np
import pandas as pd

def do_it():
        """grab dfs from url and create csc for analysis"""

        years = [str(y) for y in range(2000,2020)]
        dflist = []
        
        for each in years:
                print(each)
                df = pd.read_html(f'https://www.basketball-reference.com/leagues/NBA_{each}_standings.html')
                column_name = ['Team', 'W', 'L', 'W/L%', 'GB', 'PS/G', 'PA/G', 'SRS']
                
                df1 = pd.DataFrame((df[0]))
                df1.columns = column_name
                
                df2 = pd.DataFrame((df[1]))
                df2.columns = column_name
                
                dfs = [df1,df2]

                df_final = pd.concat(dfs, join = 'outer', sort=True)
                df_final = df_final.sort_values(by = 'W', ascending = False).reset_index()
                df_final = df_final.drop(columns='index')
                df_final['year'] = pd.Series(data = f'{each}',index=df_final.index)

                dflist.append(df_final)
        
        dfs = pd.concat(dflist, join = 'outer', sort=True)
        dfs.to_csv(r"C:\Users\wilso\Desktop\NBA_Analysis\NBA_Trends\data\standings.csv", sep=',', encoding='utf-8')

if __name__ == "__main__":
        
        do_it()
