n=371
m=n
sum=0

while n!=0:
    dgt=n%10
    dgt=dgt**3
    sum+=dgt
    n=n//10

if m==sum:
    print("It is a armstrong number.")
else:
    print("It is not a armstrong number.")
      