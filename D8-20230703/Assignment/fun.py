def call_interest(p,n,r):
     interest = p*n*r/100
     return interest
p = 1000
n = 10
r = 2
interest = p*n*r/100
print(interest)

def eligible_for_vote(age):
     if age>17:
         return ("eligible for vote")
     else:
         return(" not eligible for vote")
eligible = eligible_for_vote(16)
print(eligible)




def check_odd_even(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
    # b = num * num2
    # return b
result = check_odd_even(47)
result2 = check_odd_even(10)
print(result)
print(result2)





