n=int(input("Enter any number:"))

a=0
b=1
print(f"{a} {b}",end=" ")
for i in range(1,n+1,1):
    c=a+b
    print(c,end=" ")
    a=b
    b=c