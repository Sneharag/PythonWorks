
num=int(input("Enter number: "))

prev=0

current=1

if num==0:

    print(1)

elif num==1:

    print(1)

else:

    for i in range(1,num+1):

       next=prev+current

       if(next>num):

          print(next)

          break

       prev=current

       current=next


