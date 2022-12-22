a=int(input("Enter first number"))
b=int(input("Enter second number"))
op=input("Enter operator")
match(op):
    case '+':
        print(f"Sum={a+b}")
    case '-':
        print(f"Difference={a-b}")
    case _:
        print("no such operator ")