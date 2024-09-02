numbers=[10,11,12,13,14,20,21]
#print prime number from the numbers

for i in numbers:

    for j in range(2,i):

        if i%j!=0:

            print(i)
            break

