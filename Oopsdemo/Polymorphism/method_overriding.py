# method overriding - 

class Parent:

    def bike(self):

        print("passion pro")

    def mobile(self):

        print("samsung")

class Child(Parent):

    def mobile(self):

        print("Iphone")

    def bike(self):

        print("hunter")

child_instance=Child()

child_instance.bike()

child_instance.mobile()


    