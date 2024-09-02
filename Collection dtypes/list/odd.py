#prgm to return the odd numbers in a list

num=[1,2,3,4,5,6,7]

odd=[]

for i in num:

    if i%2!=0:

        odd.append(i)

print(odd)