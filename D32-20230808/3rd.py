import json
input=(input("nums:"))
list=json.loads(input)
majority_num=0
for i in list:
    num=list.count(i)
    if num>majority_num:
        majority_num=num
        ans=i
print(ans)





