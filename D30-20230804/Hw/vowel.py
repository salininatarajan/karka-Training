sentence=input("enter the sentence :")
def vowels_count(word):
    vowels=["a","e","i","o","u"]
    count=0
    for i in word:
      if i.lower()in vowels:
            count+=1
    return count
def max_vowel_word(sentence):
    without_empty_space=sentence.strip()
    value=without_empty_space.split()
    max_words=""
    max_count=0

    for i in value:
        count=vowels_count(i)
        if count>max_count:
            max_count=count
            max_word=i
    return max_word
print(max_vowel_word(sentence))




nums=[2,3,5,6,4,7,9,8,5]
sum=9
def target_sum(nums,sum):
    tup=()
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==sum  :
                tup+=((nums[i],nums[j]),)

    return tup
print(target_sum(nums,sum))




