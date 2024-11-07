# ebook.py

class EBook:
    """
    Represents an e-book in the store catalog with details like title, author, publication date, genre, and price.
    This class includes methods to add, modify, and remove e-book details.
    """
    
    def __init__(self, title, author, publication_date, genre, price):
        """
        Initialize the e-book with essential details like title, author, publication date, genre, and price.
        """
        self.__title = title
        self.__author = author
        self.__publication_date = publication_date
        self.__genre = genre
        self.__price = price

    # Getter and setter methods for title
    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    # Getter and setter methods for author
    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    # Getter and setter methods for price
    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    # Getter and setter methods for genre
    def get_genre(self):
        return self.__genre

    def set_genre(self, genre):
        self.__genre = genre

    # Getter and setter methods for publication date
    def get_publication_date(self):
        return self.__publication_date

    def set_publication_date(self, publication_date):
        self.__publication_date = publication_date

    def __str__(self):
        """
        Returns a string representation of the e-book with its details.
        """
        return "EBook(title='" + self.__title + "', author='" + self.__author + "', genre='" + self.__genre + "', publication_date='" + self.__publication_date + "', price=" + str(self.__price) + ")"

    # Method to update e-book details (title, author, price, etc.)
    def update_ebook_details(self, title=None, author=None, publication_date=None, genre=None, price=None):
        """Update e-book details selectively."""
        if title:
            self.set_title(title)
        if author:
            self.set_author(author)
        if publication_date:
            self.set_publication_date(publication_date)
        if genre:
            self.set_genre(genre)
        if price:
            self.set_price(price)

    # Method to remove e-book details (resetting attributes to None)
    def remove_ebook_details(self):
        """Remove e-book details by setting them to None."""
        self.__title = None
        self.__author = None
        self.__publication_date = None
        self.__genre = None
        self.__price = None
