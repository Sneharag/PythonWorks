
from re import fullmatch

var=input("Enter variable name: ")

pattern="[a-zA-Z][a-zA-Z0-9_]*"

matcher=fullmatch(pattern,var)

print("invalid" if matcher==None else "Valid")