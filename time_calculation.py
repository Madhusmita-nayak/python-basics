a=int(input("Enter any number:"))

h=a//3600
m=(a%3600)//60
a=((a%3600)%60)%60
print(f"The seconds after conversion {h}hr::{m}min::{a}sec")