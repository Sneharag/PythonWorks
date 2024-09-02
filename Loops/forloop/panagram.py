
text="The quick brown fox jumps over a lazy dog"

text=text.casefold()

is_panagram=True

alphabets="abcdefghijklmnopqrstuvwxyz"

for ch in alphabets:

    if text.count(ch)==0:

        is_panagram=False
        break

print(is_panagram)





