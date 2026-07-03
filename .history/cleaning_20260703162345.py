import pandas as pd 

df = pd.read_csv('data.csv')
# print(df)
# new_dataframe = df.dropna()
# print(new_dataframe.to_string())

# if we want to return the original dataframe then inplace = True attribute 

df.dropna(inplace=True)
print(df.to_string())