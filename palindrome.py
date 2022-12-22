n=int(input("Enter any number:"))
m=n
rev=0

while n!=0:
    dgt=n%10
    rev=rev*10+dgt
    n=n//10

if rev==m:
    print("It is a palindrome number.")
else:
    print("It is not a palindrome number.")