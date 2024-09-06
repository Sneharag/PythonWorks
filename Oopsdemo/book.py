

class Book:

    title:str
    author:str
    price:int
    language:str

    def __init__(self,title,author,price,language):
        
        self.title=title
        self.author=author
        self.price=price
        self.language=language

    def display_book(self):

        print(self.title,self.author,self.price,self.language)

book_instance1=Book("Atomic Habits","James Clear",350,"English")
book_instance2=Book("The Alchemist","Paulo Coulo",450,"English")
book_instance1.display_book()
book_instance2.display_book()