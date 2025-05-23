
# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.
class Book:
    count = 0

    @classmethod
    def increment_book_count(cls):
        cls.count +=1

book:Book= Book.increment_book_count()
book = Book.increment_book_count()
print(Book.count)

