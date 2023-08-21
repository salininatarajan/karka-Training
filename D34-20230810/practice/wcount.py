# list=[1,2,1,3,3]
# for i in list:
#     num=list.count(i)
#     if num ==1:
#         print("constant value :",i)

list=[1,2,3,3,1]
dic={}
for i in list:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]=dic[i]+1
for key in dic:
    if dic[key] ==1:
        print(key)
