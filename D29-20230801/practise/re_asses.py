# list1=[1,2,3,4,5]
# list2=[5,4,3,2,1]
# list3=[]
# for i in range(len(list1)):
#     if list1[i]>list2[i]:
#         list3+=[list1[i]]
#     else:
#         list3+=[list2[i]]
# print(list3)

num=int(input("num:"))
# for i in range(num,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print("")

for i in range(1,num+1,+1):
        print(i*"*",end="")
        print("")
for i in range(num-1,0,-1):
    print(i*"*",end=" ")
    print("")

# for i in range(num*2):
#     if i<=num:
#         ans=i
#     else:
#          ans=(num*2)-i
#     for j in range(ans):
#         print("*",end="") 
#     print("")
    





