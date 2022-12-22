math=int(input("Enter the marks of maths:"))
science=int(input("Enter the marks of science:"))
english=int(input("Enter the marks of english:"))
social=int(input("Enter the marks of social:"))
literature=int(input("Enter the marks of literature:"))

total=math+science+english+social+literature
average=total/5

if average>=90:
    grade='o'
elif average>=80 and average<90:
    grade='a'
elif average>=70 and average<80:
    grade='b'
elif average>=60 and average<50:
    grade='c'
elif average>=50 and average<40:
    grade='d'
elif average>=40 and average<50:
    grade='e'
elif average<40:
    grade='f'

print(f"The given grade acquired: {grade}")