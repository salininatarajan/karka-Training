first=int(input("enter your number"))
operator = input("enter your operator")
second = int(input("enter your number"))
def arthmetic_operations(num1,operator,num2):
    if operator=="+":
        return(num1+num2)
    if operator=="-":
        return(num1-num2)
    if operator=="*":
        return(num1*num2)
    if operator=="/":
        return(num1/num2)
    if operator=="**":
        return(num1**num2)
result =  arthmetic_operations(first,operator,second)
print(result)




      
    
    


    