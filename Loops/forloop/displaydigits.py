#print alphabets

word="i have 2 car and 1 bike"

for ch in word:

    if ch.isalpha():

        print(ch,end=",")

#print digits

print()

for ch in word:

    if ch.isdigit():

        print(ch,end=",")

