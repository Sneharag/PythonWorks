
class Dishes:

    name:str
    price:int
    qty:str

    def __init__(self,name,price,qty):

        self.name=name
        self.price=price
        self.qty=qty

    def __str__(self):

        return self.name        
    

class Restraunt:

    name:str
    place:str
    dishes=[]

    def __init__(self,name,place):
            
        self.name=name
        self.place=place

    def add_dishes(self,dish):

        self.dishes.append(dish)

    def list_dishes(self):

        for d in self.dishes:

            print(d)

idli_instance=Dishes("idli",40,"medium")
puttu_instance=Dishes("puttu",30,"large")
dosa_instance=Dishes("masala dosa",45,"medium")

restraunt_instance=Restraunt("Ananda Bhavan","Kannur")

restraunt_instance.add_dishes(idli_instance)
restraunt_instance.add_dishes(puttu_instance)

restraunt_instance.list_dishes()

restraunt_instance2=Restraunt("Cofee House","Kannur")

restraunt_instance2.add_dishes(dosa_instance)
restraunt_instance2.list_dishes()