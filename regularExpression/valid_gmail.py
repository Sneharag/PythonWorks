# valid gmail
# start with alphanumeric
#[a-zA-Z0-9._]

from re import fullmatch

email=input("enter email: ")

pattern="\\w[\\w._]*(@gmail.com)"

matcher=fullmatch(pattern,email)

print("Invalid" if matcher==None else "Valid")