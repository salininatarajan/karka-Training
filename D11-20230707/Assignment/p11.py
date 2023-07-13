weight = int(input(f" please enter your current earth weight:"))
planet = int(input(f"""
I have information for the following planets :
    1. venus       2.Mars      3.Jupiter
    4. Saturn      5.Uranus    6.Neptune
               
which planet are you vissting?"""))
def relative_gravity (weight,planet):
    if planet==1:
        return weight*(0.78)
    elif planet==2:
        return weight*(0.39)
    elif planet==3:
        return weight*(2.65)
    elif planet ==4:
        return weight*(1.17)
    elif planet==5:
        return weight*(1.05)
    elif planet == 6:
        return weight*(1.23)
    
result = relative_gravity(weight,planet)
print(f" your weight would be {result} pounds on that planet.")











