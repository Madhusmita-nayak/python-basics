a=int(input("Enter any number:"))
m=a
sum=0

for a in range(a-1,0,-1):
    if m%a==0:
        sum+=a

if sum==m:
    print("It is perfect number.")
else:
    print("It is not a perfect number.")