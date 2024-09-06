
class Bike:

    name:str
    brand:str
    price:int

    def __init__(self,name,brand,price):

        self.name=name
        self.brand=brand
        self.price=price

    def __str__(self):

        return self.name
    

class ShowRoom:

    name:str
    place:str
    bikes:list

    def __init__(self,name,place):

        self.name=name
        self.place=place
        self.bikes=[]

    def add_vehicle(self,bike):

        self.bikes.append(bike)

    def list_vehicles(self):

        for b in self.bikes:

            print(b)

hunter_instance=Bike("hunter","re",200000)
activa_instance=Bike("activa","hinda",100000)
dominar_instance=Bike("dominar","bajaj",120000)

showroom_instance=ShowRoom("popular","Kakkanad")

showroom_instance.add_vehicle(hunter_instance)

showroom_instance.add_vehicle(dominar_instance)

showroom_instance.list_vehicles()

showroom_instance2=ShowRoom("tags","thrissur")

showroom_instance2.add_vehicle(hunter_instance)
showroom_instance2.add_vehicle(activa_instance)
showroom_instance2.add_vehicle(dominar_instance)

showroom_instance2.list_vehicles()
