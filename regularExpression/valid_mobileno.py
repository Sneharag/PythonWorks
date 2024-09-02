
#validate mobile no with country code

from re import fullmatch

mobileno=input("Enter phone no: ")

pattern="(91)\\s?[6789]\\d{9}"

matcher=fullmatch(pattern,mobileno)

print("Invalid" if matcher==None else "Valid")