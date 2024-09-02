#print first recursive character

text="ABCADD"

word_count={}

for i in text:

    if i in word_count:

        word_count[i]+=1

        print(f"{i}-first recursive character")

        break

    else:

        word_count[i]=1

