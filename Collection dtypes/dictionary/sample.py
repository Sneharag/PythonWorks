#key should be unique


# student={"name":"Sneha","course":"Python","course":"datascience"}
# print(student)     

# student["name"]="Rahul"   #updates 


#update the course as fullstack in students using iteration

student={"name":"Sneha","course":"Python","place":"chennai"}

for i in student:

    if i=="course":

        student[i]="Fullstack"
    
print(student)


#delete a key "place" if it present in the dict using iteration

# Iterate over a copy of the dictionary's keys to avoid runtime error
# for i in list(student.keys()):

#     if i=="place":

#         student.pop(i)

# print(student)