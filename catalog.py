class Catalog:
    """
    Represents a collection of e-books in the store. Allows adding, removing and searching e-books.
    """
    
    def __init__(self):
        self.__ebooks = []

    def add_ebook(self, ebook):
        """Adds an e-book to the catalog."""
        self.__ebooks.append(ebook)

    def remove_ebook(self, title):
        """Removes an e-book by title."""
        self.__ebooks = [ebook for ebook in self.__ebooks if ebook.get_title() != title]

    def search_by_title(self, title):
        """Finds an e-book by title."""
        for ebook in self.__ebooks:
            if ebook.get_title() == title:
                return ebook
        return None

    def get_ebooks(self):
        return self.__ebooks

    def __str__(self):
        ebook_list = ", ".join([ebook.get_title() for ebook in self.__ebooks])
        return "Catalog(" + ebook_list + ")"
