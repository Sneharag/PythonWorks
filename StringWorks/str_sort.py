
#1
text="hello"

sort=sorted(text,reverse=False)

print(sort)

#2
def sub(num1,num2,abs=False):

    if abs==False:

        return num1-num2
    
    else:

        return num1-num2 if num1>num2 else num2-num1
    
print(sub(5,10,abs=True))