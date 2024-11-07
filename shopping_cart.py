class ShoppingCart:
    """
    Represents a shopping cart where customers can add, remove and update e-books.
    """
    
    def __init__(self):
        self.__items = {}  # Dictionary to store e-books and their quantities

    def add_ebook(self, ebook, quantity=1):
        """Add an e-book to the cart with the specified quantity."""
        if ebook in self.__items:
            self.__items[ebook] += quantity
        else:
            self.__items[ebook] = quantity

    def remove_ebook(self, ebook):
        """Remove an e-book from the cart."""
        if ebook in self.__items:
            del self.__items[ebook]

    def get_total_items(self):
        """Return total items in the cart."""
        return sum(self.__items.values())

    def get_items(self):
        return self.__items
    
    def display_cart_items(self):
        """Display each e-book title and its quantity in the cart using string concatenation."""
        if not self.__items:
            return "Your cart is empty!"
        
        cart_contents = ""
        for ebook, quantity in self.__items.items():
            cart_contents += "Title: " + ebook.get_title() + ", Quantity: " + str(quantity) + "\n"
        return cart_contents

    def __str__(self):
        return "ShoppingCart(items=" + str(self.__items) + ")"
