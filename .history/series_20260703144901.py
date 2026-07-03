import pandas as pd

a = [45, 67, 87, 32]

rs = pd.Series(a)
print(rs)

# Labels 

print(rs[0])
print(rs[3])

# Create Labels 

# with index keyword 

lst = ["Python", "Java", "PHP"]
s = pd.Series(lst, index=["P", "J", "H"])
print(s)