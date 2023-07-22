dup_list=[1,2,2,3,4,1]
empty=[]
for num in dup_list:
    if num not in empty:
        empty.append(num)
print("orginal num_list is",(empty))




