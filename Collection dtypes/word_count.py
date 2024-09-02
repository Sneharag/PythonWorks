
words=["hello","hai","hello","hai","hai","hi"]

# word_set=set(words)

# for i in word_set:
     
#     print(i,words.count(i))


word_count={}

for i in words:

    if i in word_count:

        word_count[i]+=1

    else:

        word_count[i]=1
    
print(word_count)

