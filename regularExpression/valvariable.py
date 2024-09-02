#variable name
#first char must be alphabet=k to m
#second letter must be a no. that is / 3
#followed by any number of alphabets and numbers @

from re import fullmatch

var=input("Enter variable name: ")

pattern="[k-m][369][a-zA-Z0-9@]*"

matcher=fullmatch(pattern,var)

print("Invalid" if matcher==None else "Valid")