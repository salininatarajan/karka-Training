number = int(input("Enter the number: "))

def find_index(number):
    num_list = [20, 23, 45, 67]
    for i, num in enumerate(num_list):
        if num == number:
            return i
        
print(find_index(number))

# def index(num_list):
#     for i,num in enumerate(num_list):
#         if num==85:
#             return i
# print(index([10,67,89,85,99]))


# def my_fav_friend (friend_list):
#    for friend in (friend_list):
#       if friend == ("sree"):
#          return friend
# result = (my_fav_friend(["jyo","adlins","abi","sree","thanu","carolin"]))
# print("my favourite frnd name is ",result)


# def find_index(friend_list):
#    for i,friend in enumerate(friend_list):
#       if friend == ("sree"):
#          return i
# index=(find_index(["jyo","adlins","abi","sree","thanu","carolin"]))
# print("friend name index is",index)

# def find_length(friend_list):
#    name = "jyo"
#    for i,friend in enumerate(friend_list):
#         if len(friend) > len(name):
#          name = friend
#    return name
# length = find_length(["jyo","adlin","abi","sree","carolin","thanu","sathya"])
# print("heighest name length is",length)










































