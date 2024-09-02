#fibonacci series
#0 1 1 2 3 5 8 13 21 34 . . .  .

num=int(input("Enter limit: "))

prev=0

current=1

print(f"{prev},{current}",end=",")

for i in range(1,num):

    next=prev+current

    prev=current

    current=next

    print(f"{next}",end=",")

