# sentence=input("enther the sentence:")
# value=sentence.split()
# dic={}
# for i in value:
#     count=value.count(i)
#     dic[i]=count
# print(dic)


# list=[2,5,8,1,9,3,7]
# max=0
# for i in range(len(list)):
#     for j in range(i+1,len(list)):
#         if list[j]-list[i]>max:
#             diff=list[j]-list[i]
#             max=diff
#             num1=list[j]
#             num2=list[i]
# print(f"{max}({num1}-{num2})")
           

list=[6,3,1,11,15]
max=0
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]>list[j]:
            diff=list[i]-list[j]
            num1=list[i]
            num2=list[j]
        else:
            diff=list[j]-list[i]
            num1=list[j]
            num2=list[i]
        if diff>max:
            max=diff
            one=num1
            two=num2
print(f"{max}({one}-{two})")







           