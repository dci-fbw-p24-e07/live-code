from author import Author
from book import Book


class BookTest:
    def __init__(*args):
        author1 = Author("John Brown", "jbrown@mail.com", "Male")
        author2 = Author("Sylvia Foster", "sfoster@books.com", "Female")
        author3 = Author("Dr. Richard Castle", "drcastle@mail.com", "Male")

        print(author1)
        print(author2)
        print(author3)  # Test __str__(self)
        author3.set_email("changedemail@email.com")  # Test email setter
        print("name is: " + author3.get_name())  # Test getter
        print("email is: " + author3.get_email())  # Test getter
        print("gender is: " + author3.get_gender())  # Test getter
        print(
            "Author after changed email: "
            + str(author3)  # pay attention! author3 now has a changed email
        )
        print("========================")

        book1 = Book("The Python Journey", author3, 65.50, 1000)
        book2 = Book("Java Sucks", author2, 20, 100000)
        book3 = Book("JavaScript: The language of everything", author1, 99.99, 10000)

        print(book1)
        print(book2)
        print(book3)

        # Test Getters and Setters
        book3.set_price(29.95)
        book3.set_qty(28)
        print("name is: " + book3.get_name())
        print("price is: " + str(book3.get_price()))
        print("qty is: " + str(book3.get_qty()))
        print("Author is: " + str(book3.get_author()))
        # Author's __str__(self)
        print("Author's name is: " + book3.get_author().get_name())
        print("Author's email is: " + book3.get_author().get_email())
        print("Book after changed price and quantity: " + str(book3))
