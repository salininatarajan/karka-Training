nums=[[1,2],[3,4]]
input=input("enter the operator:")
plus=0
list=[]
for num in nums:
    for i in num:
        if input=="add":
            plus=plus+i
        elif input=="string":
            list+=[i]
print(plus)
print(list)

        
