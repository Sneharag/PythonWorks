
num=int(input("Enter the number: "))

prev=0

#is_fibo=False

current=1

if num in (0,1):

    print("Fibonacci no.") 
    #is_fibo=True
else:

    next=1

    while(next<=num):
        
        next=prev+current
        
        if next==num:
            
            print("It is a fibonacci no.")
            #is_fibo=True

            break

        prev=current

        current=next
if next!=num:
    print("Not a fibonacci no.")
#print(is_fibo)

