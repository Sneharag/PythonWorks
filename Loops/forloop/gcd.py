# gcd of two numbers

num1=int(input("Enter first number: "))

num2=int(input("Enter second number: "))

gcd=1

for i in range(1,num1+1):

    if num1%i==0 and num2%i==0:

        gcd=i

print(f"gcd of {num1},{num2}={gcd}")



