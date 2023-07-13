name = input(f"Hey, What's your name?")
age = int(input(f"ok,{name}, how old are you ?:"))
def is_eligible(age):
    if age<16:
        print("you can't drive,",name)
    if age<18 :
        print("you can't vote,",name)
    if age<25:
        print("you can't rent a car",name)
    if age>=25:
        print("you can do anything that's legal",name)
result = is_eligible(age)
print(result)



         