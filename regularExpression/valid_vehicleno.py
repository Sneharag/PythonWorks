
#kerala vehicle reg no validation

#starting with KL
#two digits
#alphabets[]
#4digits

from re import fullmatch

var="KL13M3861"

pattern="(KL)(-)?[0-9]{2}(-)?[A-Z]{1,2}(-)?[0-9]{4}"

matcher=fullmatch(pattern,var)

print("Invalid" if matcher==None else "Valid")


# ? - atmost one/optional
# * - 0 or more
# + - match one or more