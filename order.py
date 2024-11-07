class Order:
    """
    Represents an order for e-books. Includes customer and shopping cart and creates an invoice.
    """
    
    def __init__(self, customer, cart):
        self.__customer = customer
        self.__cart = cart

    def get_customer(self):
        return self.__customer

    def get_cart(self):
        return self.__cart

    def __str__(self):
        return "Order(customer='" + self.__customer.get_name() + "', cart=" + str(self.__cart) + ")"
