num1=int(input("\nEnter first no.: "))

num2=int(input("\nEnter second no.: "))

num3=int(input("\nEnter third no.: "))

if num1>num2 and num1>num3:

    if num2>num3:

        print(f"{num2} is second largest")

    else:

        print(f"{num3} is second largest")

elif num2>num1 and num2>num3:

    if num1>num3:
        
        print(f"{num1} is second largest")

    else:

        print(f"{num3} is second largest")

else:
    
    if num1>num2:
        
        print(f"{num1} is second largest")

    else:

        print(f"{num2} is second largest")
