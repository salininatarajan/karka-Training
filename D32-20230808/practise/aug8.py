# days=int(input("N:"))
# list=[]
# for i in range(1,days+1):
#     cost=int(input("each_day_cost:"))
#     list.append(cost)
# min=list[0]
# max=0
# for i,rate in (list):
#     if rate<min:
#         min=rate
#         out1=i
# for j in range(out1,len(list)):
#     if rate>max:
#         max=rate
#         out2=i
# print(out1,out2)



days=int(input("N:"))
list=[]
for i in range(1,days+1):
    cost=int(input("each_day_cost:"))
    list.append(cost)
profit=0
for i in range(len(list)):
    for j in range(i+1,len(list)):
            dif=list[j]-list[i]
            if dif>profit:
                profit=dif
                num1=i+1
                num2=j+1
       
print(num1,num2)








