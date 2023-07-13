def gender():    
    gender=input("What is your gender (M or F):")
    name1=input("Fisrt name :")
    name2=(input("Last name :"))
    age= int(input("Age:"))
    qsn=input(f"Are you married, {name1} (y or n)?")
    if gender=="male":
        if age>20:
            if qsn=="yes":
                print(f" shall I call you ,Mr{name1}{name2}")
            elif qsn=="no":
                print(f"{name1}{name2}")  
        else :
              print(f"{name1}{name2}")  
            

            
    elif gender=="female":
        if age>20 :
            if qsn=="yes":
                print(f" shall I call you ,Mrs{name1}{name2}")
            elif qsn =="no":
                print(f"Ms{name1}{name2}")  
        else:
              print(f"{name1}{name2}")  
gender()












