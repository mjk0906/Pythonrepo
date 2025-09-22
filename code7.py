grade=["A","B","C","D","E","FAIL"]
print(grade.count("A"))
grade.sort(reverse=True)
print(grade)

#dictionary 
info={
    "name":"Jayant",
    "age":18,
    "college":"IIT",
    "games":["cricket","BGMI","Call of Duty","Free Fire"],
    "marks": 97.7 
}

print(info["games"])

set1= {1,2,3,4,5,6,7,"amma",9}
print(set1)
print(type(set1))
print(len(set1))
emptyset=set()
set2={10,7,8}
print(set1.union(set2))
#verygood 

meanings={
    "table":["furniture", "list of facts and figures"] ,
    "cat":"a pet animal"

}

subjects={"python","java","c++","python","js","java","pthon","java","c++","c"}
print(len(subjects))
print(subjects)

#loops 

count=1
while(count<=1):
    print("paradise")
    count+=1

print("loop ended")     

i=1
while(i<=10):
    print(3*i)
    i+=1

nums=[1,4,9,16,25,36,49,64,81,100]
j=0
while(j<=len(nums)):
    print(nums[j])
    j+=1
