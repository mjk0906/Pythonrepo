
#loops 

count=1
while(count<=1):
    print("paradise")
    count+=1

print("loop ended")     


nums=[1,4,9,16,25,36,49,64,81,100]
j=0
x=36
while j<len(nums):
    if nums[j]==x:
        print("found at index: ",j)
    else:
        print("finding the value,current index:",j)
    j+=1
    
i=1
while(i<=10):
    if i%2==0:
        i+=1
        
        continue
    print(i)    #skipped in the code when the output was 3 so we added one more i+=1 in the if block
    i+=1
    
values= [1,2,3,4,5,6,7,8,9,10]
x=2
idx=0
for val in values:

    if val==x:
        print("the value of x is found",idx)
    idx+=1
seq=range(10)
for i in seq:
    print(i)
for i in range(5):
    print(i)
for i in range(2,101,2):
    print(i)

for i in range(9):
    pass 

n=5
prod=1
i=1
while i<=5:
    prod=prod*i
    i+=1
print("the product is total :",prod)
  
#functions in python 
def calc_sum(a,b):
    sum=a+b
    print("the sum is function",sum)
    return sum 

calc_sum(4,5)
A=["ironman","superman","batman","captain america"]

def print_len(list):
    print(len(list))
    
print_len(A)

def print_list(list):
    for item in list:
        print(item,end="\n")

print_list(A)




