import pandas as pd 

employee_details = {
    "EmployeeName": ["Raj", "Shiva", "Savita"],
    "Department": ["IT", "HR", "IT"],
    "Salary": [5600, 7800, 54000]
}

df = pd.DataFrame(employee_details)
df.to_csv("employee.csv", index = False)

result = df[df["Salary"] > 7800]
print(result)

res = df.groupby("Department")["Salary"].mean()
print(res)

res1 = df["Department"].value_counts()
print(res1)

res2 = df.groupby("Department").size()
print(res2)

res3 = df.sort_values("Salary", ascending=False)
print(res3)

# 1. Read a CSV File

df = pd.read_csv("data.csv")
# print(df.to_string())

# print(df.head())

# 3. Check Data Information

# print(df.info())
# 
# 4. Find Missing Values

# print("missing values", df.isnull())
print("Missing values count", df.isnull().sum())