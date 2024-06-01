# Create a class called library with data attributes like acc_number, 
# publisher, title and author. The methods of the class should include
# a. read() – acc_number, title, author.
# b. compute() - to accept the number of days late, calculate and 
# display the fine charged at the rate of $1.50 per day.
# c. display the data.

class Library:
    def __init__(self,acc_number,publisher,title,author):
        self.acc_number = acc_number
        self.publisher = publisher
        self.title = title
        self.author = author
        self.days_late = 0

    def read(self):
        print("Acc no.:",self.acc_number)
        print("Title:",self.title)
        print("Author:",self.author)

    def compute(self):
        fine = self.days_late * 1.50
        print("Fine charged: $",fine)

    def display(self):
        print("Acc no.:",self.acc_number)
        print("Publisher:",self.publisher)
        print("Title:",self.title)
        print("Author:",self.author)

book = Library(123,"Chapman & Hall","Great Expectations","Charles Dickens")
book.read()
book.days_late = int(input("Enter no. of days late: "))
book.compute()
book.display()