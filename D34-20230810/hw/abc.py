input="abcabcbb"
output=""
for i in input:
    if i not in output:
        output+=i
print("the ans is",output,"with the length",len(output))

