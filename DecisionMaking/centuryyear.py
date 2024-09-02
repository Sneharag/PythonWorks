# read a year from user
#print century year if year ends with two zeros
#else print non century year

year=int(input("\nEnter a year: "))

if year%100==0:

    print("Century year")

else:

    print("Non Century year")