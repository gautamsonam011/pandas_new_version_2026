import pandas as pd 

df = pd.read_csv('data.csv')
# print(df)
# new_dataframe = df.dropna()
# print(new_dataframe.to_string())

# if we want to return the original dataframe then inplace = True attribute 

df.dropna(inplace=True)
print(df.to_string())

# Replace empty values 

# fillna() method 

data = {
    "EmployeeName": ["Raj", "Geeta", "Jiya", "John"],
    "EmployeeID": ["raj1", "geeta2", "jiya3", "john4"],
    "Salary": [50000, 60000, 80000, 30000]
}

df = pd.DataFrame(data)


