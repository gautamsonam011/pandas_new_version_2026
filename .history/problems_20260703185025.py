# 9. Can you get items of series A that are not available in another series B?
import pandas as pd

df1 = pd.Series([2, 4, 8, 10, 12])
df2 = pd.Series([8, 12, 10, 15, 16])

df1 = df1[~df1.isin(df2)]
print(df1)

# How will you get the items that are not common to both the given series A and B?
import numpy as np 

unique = np.union1d(df1, df2)
print(unique)

matched = np.intersect1d(df1, df2)
print(matched)

# How do you write a DataFrame to CSV?

data = {
    "subjects": ["cd", "ds"],
    "marks": [45, 67]
}

df = pd.DataFrame(data)

df.to_csv("output.csv", index=False)
# print(df)

# print(df.iloc[0])
print(df.loc[[0, 1]])

