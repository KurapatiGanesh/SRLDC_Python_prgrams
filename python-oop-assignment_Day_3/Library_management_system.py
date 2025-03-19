class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
    def __str__(self):
        return f"Title:{self.title} Author Name: {self.author} ISBN :{self.isbn}"

class Library:
    def __init__(self):
        self.books=[]
    
    def add_books(self,book):  #Books Add Method
        self.books.append(book)
        print(f"{book.title} Book Add Sucessfully")

    def remove_book(self,isbn): #Remove Books Method 
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book '{book.title}' removed Sucess fully")
                return
        print("Book Not in Library")

    def display_Books(self): #Display All Books In library
        if not self.books:
            print("No any Book in Library")
        else:
            print("Books Datails:")
            for book in self.books:
                print(book)


library=Library()
book1=Book("Mahabharat","Vyas","B100")
book2=Book("Ramayan","Valmiki","B200")
book3=Book("Maths","Ramanuj","B300")
library.add_books(book1)
library.add_books(book2)
library.add_books(book3)
library.remove_book("B200")
library.display_Books()
