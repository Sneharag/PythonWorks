#sum of all even numbers from 1 to 100

sum=0

for i in range(1,101):

    if i%2==0:

        sum=sum+i
    
    i+=1

print(sum)