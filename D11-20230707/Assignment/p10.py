name = input(f"Hey, What's your name? (Sorry, I keep forgetting.)")
age = int(input(f"ok,{name}, how old are you ?:"))
def is_eligible(age):
    if age<16:
        print("you can't drive.",name)
    elif 16<=age<=17:
        print("you can drive but not vote,",name)
    elif 18<=age<=24:
        print("you can vote but not rent a car.",name)
    elif age>=25:
        print("you can do pretty much anything.",name)
(is_eligible(age))
