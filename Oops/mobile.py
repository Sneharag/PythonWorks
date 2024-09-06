
class Mobile:

    name:str
    storage:str
    price:int
    brand:str

    def __init__(self,name,storage,price,brand):

        self.name=name
        self.storage=storage
        self.price=price
        self.brand=brand

    def display_mob(self):

        print(self.name,self.storage,self.price,self.brand)

    def __str__(self):

        return self.name
    
mob_instance=Mobile("nord123","128",18000,"oneplus")

print(mob_instance)