n=int(input("Enter the starting range:"))
m=int(input("Enter the ending range:"))

print("The even numbers =",end="\n")
for i in range(n,m+1,1):
    if i%2==0:
        print(i,sep=" ")

print("The odd numbers =",end="\n")
for i in range(n,m+1,1):
    if i%2!=0:
        print(i,sep=" ")