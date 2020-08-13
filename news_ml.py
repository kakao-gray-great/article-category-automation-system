import pandas as pd

df = pd.read_csv("./news.tsv", delimiter="\t")
print(df.head(100))