import pandas as pd 

df = pd.read_csv('data.csv')
new_dataframe = df.dropna()
print(new_dataframe.to_string())