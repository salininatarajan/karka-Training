input=[1,2,3,4]
num=""
list=[]
for i in input:
    num=num+str(i)
total=int(num)+1
ans=str(total)
for j in ans:
    list.append(int(j))
print(list)


