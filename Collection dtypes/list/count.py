#prgrm to print unique elements in list

num=[1,2,2,3,4,5,3,6,4,7]

for i in num:

    if num.count(i)==1:

        print(i)