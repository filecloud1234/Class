b = int(input("Enter Your Base:"))
e = int(input("Enter Your Exponent:"))

result = 1 

while e > 0:
    result = result * b
    e = e - 1

print(result)
