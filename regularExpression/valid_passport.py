# It should consist of eight characters.
# The first character must be an uppercase alphabet.
# The next two characters - first character ranging from 1 to 9 
#  the second character from 0 to 9.
# 4th zero or one white space .
# four characters can be any number from 0 to 9.
# The last character  1 to 9.

from re import fullmatch

passport=input("Enter passport no: ")

pattern="[A-Z][1-9]\\d[0|\\s]\\d{4}[1-9]"

matcher=fullmatch(pattern,passport)

print("Invalid" if matcher==None else "Valid")