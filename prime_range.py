n=int(input("Enter any number:"))
sum=0

for r in range(1,n+2,1):
    for i in range(1,r,1):
     if r%i==0:
        sum+=1
    if sum==1:
        print(r)