#is_amstrong no. or not

def is_amstrong(num):

    sum=0

    number=num

    digit_count=len(str(num))

    while(num!=0):
        
        digit=num%10
        
        expo=digit**digit_count

        sum=sum+expo

        num=num//10

    if number==sum:

        return True
    
    else:
        
        return False
    
print(is_amstrong(153))