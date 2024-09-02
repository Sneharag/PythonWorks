#read a no. from user
#print fizz if num / by 3
#print buzz if num / by 5
#print fizzbuzz if num is / by 15

num=int(input("\nEnter a no.: "))

if num%15==0:

    print("FizzBuzz")

elif num%5==0:

    print("Buzz")

elif num%3==0:

    print("Fizz")

else:

    print("Invalid no.")