#sum of all odd no. from 1 to 100

i=1

sum=0

while(i<=100):

    if i%2!=0:

        sum=sum+i
    
    i+=1

print(sum)