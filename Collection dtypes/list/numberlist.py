#print no of objects in numbers
#print even numbers from this numbers
#print total of numbers
#print total of odd numbers

numbers=[10,11,12,34,43,54,78,42]

print(f"Length:{len(numbers)}")

print("\nEven numbers:")
for i in range(0,len(numbers)):

    if numbers[i]%2==0:

        print(numbers[i])

sum=0
for i in range(0,len(numbers)):

    sum=sum+numbers[i]

print(f"\nSum: {sum}")

sum=0
for i in range(0,len(numbers)):

    if numbers[i]%2!=0:

        sum=sum+numbers[i]
print(f"\nOdd Sum: {sum}")