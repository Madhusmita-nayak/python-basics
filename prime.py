a=int(input("Enter any number:"))
m=a
sum=0

for a in range(a,0,-1):
    if m%a==0:
        sum+=1

if sum==2:
    print("It is a prime number.")
else:
    print("It is not a prime number.")