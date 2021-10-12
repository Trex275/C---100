#books
class Books(object):
    def __init__(self, title, author, publisher, price):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.price = price
    def read (self, title):
        print(title + " is being read right now")
Book = Books (("Simple Science - 2"), ("Dr. Satish K. Bhalghat"), ("Mandu Book House"), (380) )
print(Book.title)
Book.read("Simple SCience - 2")