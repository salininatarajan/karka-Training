user=input("enter your password (at least one uppercase letter, one lowercase letter, and one ):")
length=len(user)

def password(length):
   if length<6:
     return("weak")
   elif 6<=length<=10:
      return("moderate")
   elif 11<=length<15:
      return("strong")
   elif length>=15:
      return("very_strong")
digit=False
lower=False
upper=False
for i in user:
    if i.isdigit():
        digit=True
    elif i.islower():
        lower=True
    elif i.isupper():
        upper=True
if digit==True and lower==True and upper==True:
    output=password(length)
    print(output)
else:
   print(" pls try with another password")

 