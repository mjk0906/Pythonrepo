
#lists and tuples

marks=[959,988,977,972,809,767,490,879]

print(type(marks))      
print(marks[1])
print(marks[2]/10)


marks.sort()
print(marks)

marks.reverse()
print(marks)

games=[]
game1=input("enter the first game:")
game2=input("enter the second game:")
game3=input("enter the third game:")
games.append(game1)
games.append(game2)
games.append(game3)
print(games)


games.append(input("enter the first movie"))
print(games)

#palindrome check code 
list1=[]
list1.append(input("enter the value 1:"))
list1.append(input("enter the value 2:"))
list1.append(input("enter the value 3:"))
list1.append(input("enter the value 4:"))
list1.append(input("enter the value 5:"))
list1copy=list1.copy()
list1copy.reverse()
if(list1copy==list1):
     print("the list is palindrome in nature")
else:
     print("the list is not palindrome in nature")