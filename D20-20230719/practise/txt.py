# name={"shalu","sree","jyo","abi","adlin","sathya","carolin"}
# print(name)
# print(name)
# print(name)

# file=open("/home/salininatarajan/Documents/karka.txt","r")

# for line in file:
#     print(line)
# data=file.read()
# print(data)

# file=open("/home/salininatarajan/Documents/karka.txt","w")
# content=file.write("my fav colour is black \n fav food is biriyani")
# file.close()
# file=open("/home/salininatarajan/Documents/karka.txt","r")
# txt =file.read()
# print(txt)


# add=open("/home/salininatarajan/Documents/karka.txt","a")
# write=add.write("i am shalu \n my age is 22")
# add.close()
# file2=open("/home/salininatarajan/Documents/karka.txt","r")
# type=file2.read()
# print(type)

file=open("/home/salininatarajan/Documents/karka.txt","a")
file.write("\n my fav food is biriyani")
file.close()
file2=open("/home/salininatarajan/Documents/karka.txt","r")
txt=file2.read()
print(txt)







