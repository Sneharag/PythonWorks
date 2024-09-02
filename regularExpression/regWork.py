
from re import finditer

text="ababaabbab"

match=finditer("ab",text)

count=0

for m in match:

    print(m.start(),"==",m.group())

    count+=1

print("no. of ab=",count)