import pandas as pd

df = pd.read_csv('data.csv')

# print(df.to_string()) 

# print(df)

# head() 

# print(df.head())
print(df.tail())

# to_excel()  it uses to convert data in excel file 

exc = df.to_excel("data.xlsx", sheet_name="newData", index=True)
print(exc)