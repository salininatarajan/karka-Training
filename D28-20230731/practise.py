# number index

# list=[1,5,3,7,9,13]
# num=int(input("enter your num:"))
# for i in range(len(list)):
#     if num==list[i]:
#         print("num index is:",i)

# add number () index

# list=[1,5,3,7,9,13]
# for i in range(len(list)):
#     for j in range(i+1,len(list)):
#         if list[i]+list[j]==10:
#             print([i,j])

            
list=[1,0,3,0,9,13]
for i in list:
    if i==0:
        list.remove(i)
    if i==3:
        list.append(i)
print(list)

