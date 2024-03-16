#Palindrome without using Slicing concept
string=input("Enter a number or string: ")
length=len(string)-1
i=0
result=""
while length>=i :
    result+=string[length]
    length-=1
if result==string :
    print("Yes it is a palindrome")
else :
    print("It is not a palindrome")