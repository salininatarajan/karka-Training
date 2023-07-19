print("Ye olde keychain shoppe")
num=0
tax_per=0
tax=8.25
shipping_cost=5.00
shipping_per_keychain =1.00

def adding(num):
    add=int(input(f"you have {num} keychains. how many to add?"))
    print(f" you now have {add} keychain")
    return add
def removes(num):
    remove=int(input(f"you have {num} kechains. How many to remove?"))
    ans=num-remove
    print(f"you now have {ans} keychain")
    return ans
def order(num,tax,shipping_cost,shipping_per_keychain):
    total=num*shipping_cost+(num*shipping_per_keychain)
    tax_per=(tax*total)/100
    print(f"""you have {num} keychains.
        keychains cost $5.00 each.
        Total cost is ${tax_per}.""")
    return tax_per
def checkout(num,tax_Per):
    name=input("what is your name?") 
    print(f"""you have {num} keychains.
        keychain cost $5.00 each.
        Total coas is $ {tax_per}.
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
       tax_per= order(num,tax,shipping_cost,shipping_per_keychain)
    elif things==4:
        checkout(num,tax_per)
        break











    


























    




    

