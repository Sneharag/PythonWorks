#is_palindrome or not

def is_palindrome(num):

    number=num

    result=0

    while(num!=0):

        digit=num%10

        result=result*10+digit

        num=num//10

    if number==result:

        return True
    
    else:

        return False
    
print(is_palindrome(145))