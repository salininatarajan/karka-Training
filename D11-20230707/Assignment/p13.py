def find_something():
    object = str(input(f"""Two QUESTIONS!
    Think of an object, and I'll try to guess it.
           
    Question  1) Is it animal, vegetable, or mineral?
    """))
    size = str(input (f"""Question 2) Is it bigger than a breadbox ?
    """))
    if object =="animal":
        if size=="yes":
            ans="moose"
        elif size=="no":
            ans="sqiurrel"
    if object=="vegetable":
        if size=="yes":
            ans="watermelon"
        elif size =="no":
            ans = "carrot"
    if object == "mineral":
        if size =="yes":
            ans="paper clip"
        elif size =="no":
            ans= "camaro"
     
    print("\n")
    print(f"""My guess is that you are thinking of a {ans}.
       I would ask you if I'm right , but I don't actually care.""")
find_something()











 

    
