
# class [design pattern,template,blueprint]
# object | instance [real worl entity]

class student:

    name:str
    age:int
    gender:str
    contact:int
    course:str

    def set_stud(self,name,age,gender,contact,course):

        self.name=name
        self.age=age
        self.gender=gender
        self.contact=contact
        self.course=course

    def display_stud(self):

        print(self.name,self.age,self.gender,self.contact,self.course)


# creating objects

stud_obj=student()

stud_obj.set_stud("hari",20,"male",4567890,"django developer")
stud_obj.display_stud()