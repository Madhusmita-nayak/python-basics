a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

print(f"Before swapping the numbers wrt there position {a} {b}")

a=a+b
b=a-b
a=a-b
print(f"After swapping the numbers wrt there position {a} {b}")