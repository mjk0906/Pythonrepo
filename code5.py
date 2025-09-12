number=int(input("enter any number:"))
if (number%2==0):
     print("the number entered by you is even")
else:
     print("the number you have entered is odd")

a=int(input("enter any number:"))
b=int(input("enter any number:"))
c=int(input("enter any number:"))
if (a>b and a>c):
     print("a is the greatest number")
elif(b>c):
     print("b is the greatest number")
else:
     print("c is the greatest number")

d=int(input("enter the number 4:"))
if (a>b and a>c and a>d):
     print("the greatest number is a")
elif(b>c and b>d):
     print("the greatest number is b")
elif(c>d):
     print("the greatest number is c")
else:
     print("the greatest number is d")

e=int(input("enter any number to check whether the number is a multiple of 7 or not "))
if (e%7==0):
     print("the number entered by you is multiple of 7")
else:
     print("the number entered by you is not a multiple of 7")


#lists and tuples

marks=[959,988,977,972,809,767,490,879]
print(type(marks))

#palindrome check code 
list1=[1,2,3,2,1]
list1copy=list1.copy()
list1copy.reverse()
if(list1copy==list1):
     print("the list is palindrome in nature")
else:
     print("the list is not palindrome in nature")
