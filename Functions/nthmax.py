#create a fun nth_digit_max with two parameter num1,num2
#nth_digit_max(123,480)=123
#nth_digit_max(461,127)=127

def nth_digit_max(n1,n2):

    digit1=n1%10

    digit2=n2%10

    if digit1>digit2:

        return n1
    
    else:

        return n2
    
print(nth_digit_max(122,486))

#or

def nth_digit_max(num1,num2):

    return num1 if num1%10 > num2%10 else num2

print(nth_digit_max(210,199))