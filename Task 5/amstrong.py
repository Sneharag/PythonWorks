numbers=[151,153,154,370,371,372,373,166341,1635]
#print amstrong numbers from numbers

sum=0

for i in numbers:
    
    number=i        

    digit_count=len(str(i))

    while(i!=0):

        digit=i%10

        expo=digit**digit_count

        sum=sum+expo

        if sum==number:

            print(i)

        i=i//10
