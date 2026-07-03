import pandas as pd

data = {
    "name":["Raj", "Ravi", "Shivam", "Riya"],
    "age":[34, 56, 21, 45],
    "marks": [67, 60, 80, 65]
}

df = pd.DataFrame(data)
print(df)