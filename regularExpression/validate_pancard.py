
# validate pancard
# first 3 characters are alphabets
# 4th place PCAFHT
# 5th place alphabet
# 4 digit
# 1 alphabet  

from re import fullmatch 

pan_no=input("enter pancard no: ")

pattern="[A-Z]{3}[PCAFHT][A-Z]{1}[0-9]{4}[A-Z]{1}"

matcher=fullmatch(pattern,pan_no)

print("Invalid" if matcher==None else "Valid")