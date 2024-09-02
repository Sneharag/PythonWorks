#extract digits

num=int(input("Enter number: "))

while(num!=0):

    digit=num%10

    print(digit)

    num=num//10

    