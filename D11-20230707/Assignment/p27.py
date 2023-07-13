print("Ye olde keychain shoppe")
num=0
rs=0
def adding(num):
    add=int(input(f"you have {num} keychains. how many to add?"))
    print(f" you now have {add} keychain")
    return add
def removes(num):
    remove=int(input(f"you have {num} kechains. How many to remove?"))
    ans=num-remove
    print(f"you now have {ans} keychain")
    return ans
def order(num,):
    rs=10*num
    print(f"""you have {num} keychains.
        keychains cost $10 each.
        Total cost is ${rs}.""")
    return rs
def checkout(num,rs):
    name=input("what is your name?") 
    print(f"""you have {num} keychains.
        keychain cost $10 each.
        Total coas is $ {rs}.
        Thanks for your order,{name}!""")
while True:
    things = int(input(f"""
    1. Add keychains to order
    2. Remove keychains from other
    3. View current order
    4. checkout
                       
    please enter your choice
        """))
  
    if things==1:
        num=adding(num)
    elif things==2:
        num=removes(num)
    elif things==3:
       rs=order(num)
    elif things==4:
        checkout(num,rs)
        break





    


























    




    

