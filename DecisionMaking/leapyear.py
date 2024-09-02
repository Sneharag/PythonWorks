#prgm to check year is leapyear

year=int(input("Enter year: "))

if (year%100==0 and year%400==0) or (year%100!=0 and year%4==0):

        print(f"{year} is a Leap year")
    
else:
        
        print(f"{year} is not a leap year")