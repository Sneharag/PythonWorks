
#sample2
word1="PQRST"

word2="ABC"
#result=PAQBRCST

str=""

smallest_word=word1 if len(word1)<len(word2) else word2

for i in range(0,len(smallest_word)):
    
    str=str+word1[i]+word2[i]

if len(word1)>len(word2):

    bal=word1[len(smallest_word):]

else:

    bal=word2[len(smallest_word):]

str=str+bal
    
print(str)