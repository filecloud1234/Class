x = input("Enter Your Number: ")
z = input("Enter Your Sign: ")
y = input("Enter Your Number: ")

x = int(x)
y = int(y)

# + - * / 
if z == "+":
    print(x+y)
elif z == "-":
    print(x-y)
elif z == "*":
    print(x*y)
elif z == "/":
    print(x/y)
else:
    print("Undifined")