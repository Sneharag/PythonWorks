
class Book:

    title:str
    author:str
    price:str

    def __init__(self,title,author,price):
        
        self.title=title
        self.author=author
        self.price=price

    def __str__(self):
        
        return self.title
    
class Library:

    name:str
    place:str
    books:list

    def __init__(self,name,place):
        
        self.name=name
        self.place=place
        self.books=[]

    def add_books(self,book):

        self.books.append(book)

    def list_books(self):

        for b in self.books:

            print(b)

book1_instance=Book("Alchemist","Paulo Coulo",450)
book2_instance=Book("Atomic Habits","James Clear",300)

library_instance=Library("popular","Kakkanad")

library_instance.add_books(book1_instance)

library_instance.add_books(book2_instance)

library_instance.list_books()

