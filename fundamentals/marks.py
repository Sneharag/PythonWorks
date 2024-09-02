#write a program to read student name and 3 marks mark1,mark2,mark3
#print total mark and average mark

stud_name=input("Enter studentent name= ")

mark1=int(input("Enter mark1= "))

mark2=int(input("Enter mark2= "))

mark3=int(input("Enter mark3= "))

print(f"\nStudent name={stud_name}")

total_mark=mark1+mark2+mark3

print(f"Total mark={total_mark}")

avg=total_mark/3

print(f"Average mark={avg}")