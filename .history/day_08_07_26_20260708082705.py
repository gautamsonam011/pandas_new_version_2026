# Problem no 1: how to use try, except, and else 

try:
    num = int(input("Enter any number:"))
except ValueError:
    print("Invalid Input")
else:
    print("You entered:", num)        

# Problem No 2: 

for i in range(2):
    pass
else:
    print(i)    