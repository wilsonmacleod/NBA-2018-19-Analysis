import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

stat_list = ['PTS', 'TRB', 'AST', 'MP']
label_list = ['Points', 'Rebounds', 'Assists', 'Minutes Played']
indexer = 0

for stat in stat_list:
    df = pd.read_csv(r'C:\Users\wilso\Desktop\NBA_Analysis\MIP\data\MIP.csv').sort_values(f'{stat}', ascending=False) 
    eight_nine = df[df['Season']== '2018-19']
    seven_eight = df[df['Season']== '2017-18']
    f, ax = plt.subplots(figsize=(8, 6))
    sns.set(style="whitegrid", font_scale=1)
    sns.set_color_codes("pastel")
    sns.barplot(x=eight_nine[f'{stat}'], y="Name", orient = "h", data=df, label="18-19", color="g")
    sns.set_color_codes("muted")
    sns.barplot(x=seven_eight[f'{stat}'], y="Name", orient = "h", data=df, label="17-18", color="b",)
    ax.set(ylabel="", xlabel=f"{label_list[indexer]} Per Game", title = f"{label_list[indexer]} Increase For MIP Candidates")
    ax.legend(ncol=4, loc="lower right", frameon=True)
    sns.despine(left=True, bottom=True)
    plt.tight_layout()
    plt.savefig(fname=r'C:\Users\wilso\Desktop\NBA_Analysis\MIP\fig\MIP-{}'.format(stat))
    indexer += 1