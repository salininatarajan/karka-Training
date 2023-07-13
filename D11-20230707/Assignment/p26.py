thing = int(input(f"""
Ye plde keychain shoppe
                       
1. Add keychains to order
2. Remove keychains from other
3. View current order
4. checkout
                       
please enter your choice
        """))
print("\n")

def order_keychain():
    print("Add keychain")

def remove():
    print("remove keychain from order")

def current_order():
    print("view current order")

def checkout():
    print("checkout")

if thing==1:
    order_keychain()
elif thing==2:
    remove()
elif thing==3:
    current_order()
elif thing==4:
    checkout()












    
            
    
   