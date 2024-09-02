#print vowel count

text="Pneumonoultramicroscopicsilicovolcanoconiosis"

text=text.lower()

vowel="aeiou"

v_count=0

consonants=0

for ch in text:

    if vowel.count(ch)!=0:

        v_count+=1

    else:

        consonants+=1

print(v_count)
print(consonants)

