#check palindrome no. or not

#121 is a palindrome no.

num=int(input("Enter number: "))

number=num

result=0

while(num!=0):

    digit=num%10

    result=result*10+digit

    num=num//10

print(result)   

print("palindrome no." if number==result else "Not a palindrome")

