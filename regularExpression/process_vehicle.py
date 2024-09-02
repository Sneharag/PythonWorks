
#read from the file
# validate
# write the valid nos to another file

from re import fullmatch

f=open("D:\\PythonWorks\\regularExpression\\vehicleno.txt")

f_w=open("D:\\PythonWorks\\regularExpression\\valid_vehiclenumbers.txt","w")

pattern=pattern="(KL)\\s?[0-9]{2}\\s?[A-Z]{1,2}\\s?[0-9]{4}"

for line in f:
    
    vehicle_no=line.rstrip("\n")

    matcher=fullmatch(pattern,vehicle_no)

    if matcher!=None:

        f_w.write(vehicle_no +"\n")