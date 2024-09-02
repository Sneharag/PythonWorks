#prgrm to check if a no. is amstrong number or not
#123=1^3+2^3+3^3
#1546=1^4+5^4+4^4+6^4

num=int(input("Enter number: "))

sum=0

number=num

digit_count=len(str(num))

while(num!=0):

    digit=num%10

    expo=digit**digit_count

    sum=sum+expo

    num=num//10

print(sum)

print("Amstrong no." if number==sum else "not a amstrong no.")

