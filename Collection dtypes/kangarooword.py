#check kangaroo word or not

source_word="regulate"

target_word="rule"

word_count={}

for i in source_word:

    if i in word_count:

        word_count[i]+=1

    else:

        word_count[i]=1

print(word_count)

kangaroo_word=True

for i in target_word:

    if i in word_count and word_count.get(i)>0:

        word_count[i]-=1

    else:

        kangaroo_word=False
        break

print(kangaroo_word)