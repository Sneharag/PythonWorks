#sum of digit

num=int(input("Enter number: "))

sum=0

while(num!=0):

    digit=num%10

    num=num//10

    sum=digit+sum

print(f"Sum={sum}")