sentence=input("sentence:")
word=sentence.split(" ")
# print(word)
max=word[0]
ans=""
for i in word:
  if len(i)>len(max):
    ans=i
print(ans)
