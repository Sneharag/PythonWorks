
f=open("D:\\PythonWorks\\File programs\\students.txt","r")

students=[]

for name in f:

    students.append(name.rstrip("\n"))

print(students)