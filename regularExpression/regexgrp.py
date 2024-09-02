
from re import finditer

text="abc123 @K#7LMdef"

# pattern="[abf]" #chk for either a b or f

# pattern="[a-k]"  #print alphabets from a to k

# pattern="[a-z]" #chk for all lowercase alphabets

# pattern="[A-Z]" #chk for all uppercase alphabets

# pattern="[A-Za-z]" #chk for all alphabets

# pattern="[0-9]" #chk all digits

# pattern="[A-Za-z0-9]" #chk alphabets and digits

# pattern="[^0-9]" #chk all except digits

# pattern="[\\s]" #chk for space

# pattern="[^a-zA-Z0-9\\s]"

# pattern="\\d"  #[0-9]

# pattern="\\D"    #[^0-9]

# pattern="\\w"  #[a-zA-Z0-9]

pattern="\\W"  #[^a-zA-Z0-9]

matcher=finditer(pattern,text)

for m in matcher:

    print(m.start(),"==",m.group())