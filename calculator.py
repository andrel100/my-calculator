a = int(input("enter a number: "))
b = int(input("enter a number: "))
# operator =["+", "-", "/"]
m = input("enter an operator eg +,-,/ :")

if m == '+':
    result = a + b
elif m == "-":
    result = a - b
elif m =="/":
    result = int(a/b)
else:
    result = "invalid option"
print(result)

