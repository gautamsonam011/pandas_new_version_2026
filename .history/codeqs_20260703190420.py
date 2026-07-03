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