text="hello hai hello hai hello"

words=text.split(" ")

word_count={}

for i in words:

    if i in word_count:

        word_count[i]+=1

    else:

        word_count[i]=1

print(word_count)