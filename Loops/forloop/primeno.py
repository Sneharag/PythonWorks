#check a number is prime no. or not

num=int(input("Enter number: "))

isPrime=True

for i in range(2,num):

    if num%i==0:

        isPrime=False

        break

print("is Prime no." if isPrime==True else "Not a prime no.")