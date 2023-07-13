def tiny_adventure():

    house=str(input(f"""
    WELCOME TO MITCHELL'S TINY ADVENTURE!
            
    You are in a creepy house! Would you like to go "upstairs" or into the 
    "kitchen"?
            """))
    print("\n")

    things = str(input(f"""
    There is a long countertop with dirty dishes everywhere. Off to one side 
    there is, as you'd expect, a refrigerator . you may open the "refrigerator" 
    or look in a "cabinet" 
                """))
    print("\n")

    name = str(input(f"""
    Inside the refrigerator you see food and stuff. It looks pretty nasty.
    Would you like to eat some of the food?( "yes" or "no") 
                """))

    if house=="kitchen":
        if things=="refrigerator":
            if name=="yes":
                ans="you had a meal"
            elif name=="no":
                ans=" you die of starvation ...eventually"
        if things=="cabinet":
            if name=="yes":
                ans="dress"
            elif name=="no":
                ans=" living thing"
    
    if house=="upstairs":
        if things=="bed room":
            if name=="yes":
                ans="to sleep"
            elif name=="no":
                ans=" watch tv"
        elif things=="balcony":
            if name=="yes":
                ans="view nature"
            elif name=="no":
                ans="drink tea "
    print(ans)
tiny_adventure()










