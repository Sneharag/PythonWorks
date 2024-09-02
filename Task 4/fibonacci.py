#is_fibonacci_number or not

def is_fibo(num):

    prev=0

    current=1

    if num in (0,1):
        
        return True
    
    else:

        next=1

        while(next<=num):
            
            next=prev+current
            
            if next==num:
            
              return True 
        
              break

            prev=current

            current=next

    if next!=num:

        return False

print(is_fibo(610))    