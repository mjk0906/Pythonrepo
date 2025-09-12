# string functions 
name="jayant"
print(len(name))

print(name.endswith("n"))
print(name.capitalize())
name= name.capitalize()
print(name)
name=name.replace("a","o")
print(name)
print(name.find("o"))

name1=str(input("enter your first name:"))
print(len(name1))

price=str(input("enter the price of your macbook:"))
print(price.count("$"))
#conditional statements



    #nesting 
age1=54
if(age1>=18):
    if(age1>=80):
        print("you cannot drive due to poor senses")
    else:
        print("you can drive peacefully")
elif(age1==17):
    print("you can drive the upcoming year")
else:
        print("you cannot drive now")
   
number=int(input("enter any number:"))
if (number%2==0):
     print("the number entered by you is even")
else:
     print("the number you have entered is odd")
     