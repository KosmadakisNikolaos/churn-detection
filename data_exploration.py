import pandas as pd

df = pd.read_csv("data/transactions_1.csv")
for i in range(len(df.columns)):
    print("----------------------------")
    print(df.columns[i])
    print(df.iloc[:, i].unique())
    print(df.iloc[:, i].value_counts())
