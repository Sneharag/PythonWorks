
# class [design pattern,template,blueprint]
# object | instance [real world entity]
# self - current instance


# constructors - initialise instance variable
# __init__() - constructor
# __str__() - str representation 

class Student:

    name:str
    age:int
    gender:str
    contact:int
    course:str

    def __init__(self,name,age,gender,contact,course):

        self.name=name
        self.age=age
        self.gender=gender
        self.contact=contact
        self.course=course

    def display_stud(self):

        print(self.name,self.age,self.gender,self.contact,self.course)


# creating objects

stud_obj=Student("hari",20,"male",4567890,"django developer")

stud_obj.display_stud()