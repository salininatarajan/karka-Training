number_list= [15,25,35,45,55]
sum = 0
enum_number = enumerate(number_list)
print(enum_number)
for i, num in enum_number:
    print("entiring iteration process for :"+str(i))
    print("before",sum)
    print(num)
    sum=sum+num
    print("after",sum)
    print("exiting iteration process for:"+str(i))
    print("\n")
average = sum/len(number_list)
print(average)

# assignment 2
cost_list = [100,200,300,400,500]
empty =[]
for cost in cost_list:
    print("INR"+str(cost))
    currency_code ="INR"+str(cost)
    empty.append(currency_code)
print (empty)













    





    
    




















        





