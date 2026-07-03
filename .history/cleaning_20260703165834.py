import pandas as pd 

df = pd.read_csv('data.csv')
# print(df)
# new_dataframe = df.dropna()
# print(new_dataframe.to_string())

# if we want to return the original dataframe then inplace = True attribute 

# df.dropna(inplace=True)
# print(df.to_string())

# Replace empty values 

# fillna() method 

# data = {
#     "EmployeeName": ["Raj", "Geeta", "Jiya", "John"],
#     "EmployeeID": ["raj1", "geeta2", "jiya3", "john4"],
#     "Salary": [50000, 60000, 80000, 30000]
# }

# df = pd.DataFrame(data)

# print(df.to_string())

# df.fillna(130, inplace=True)
# df.fillna({"Calories": 130}, inplace=True)
# print(df.to_string())

# mean() the average value (the sum of all values divided by number of values) 

# x = df["Calories"].mean()
# df.fillna({"Calories": x}, inplace=True)

x = df["Calories"].median()

df.fillna({"Calories": x}, inplace=True)

print(df.to_string())

# median() method => the value in the middle, after you have sorted all values ascending


