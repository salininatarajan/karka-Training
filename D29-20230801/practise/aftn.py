personal_details=[{"name":"shalu",
                   "email":"salininatarajan@gmail.com",
                   "password":"salini2000",
                   "hobbies":["song","cooking","frndschat"],
                   "friends":["sree","jyo","adlin","abi","muji"]},
                   {"name":"vinu",
                   "email":"vinusha@gmail.com",
                   "password":"vinu2002",
                   "hobbies":["song","dance","drawing"],
                   "friends":["sree","shalu","anu","abisha","gayu"]},
                    {"name":"gayu",
                   "email":"sivagayathri@gmail.com",
                   "password":"sivu2002",
                   "hobbies":["movies","dance","drawing"],
                   "friends":["gayu","shalu","sivu","abisha","gayu"]},]
user_email=input("enter your email :")
user_password=input("enter your password:")
def list_convert(hob):
    output = ""
    for i in hob:
        output = output + i + ","
    return output[:-1]
for i in personal_details:
   if i["email"]==user_email and i["password"]==user_password:
      i["loggin"]=True
      hob=i["hobbies"]
      frnd=i["friends"]
      print(i)
      print("Your hobbies are :",list_convert(hob))
      print("Your frnds are :",list_convert(frnd))
   else:
      i["loggin"]=False
      

    





