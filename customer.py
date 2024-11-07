# customer.py

class Customer:
    """
    Represents a customer in the e-bookstore. Contains details like name and contact information.
    It allows adding, removing, and modifying customer details.
    """
    
    def __init__(self, name, contact_info):
        """
        Initialize the customer with basic information.
        """
        self.__name = name
        self.__contact_info = contact_info

    # Getter and setter for name
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # Getter and setter for contact_info
    def get_contact_info(self):
        return self.__contact_info

    def set_contact_info(self, contact_info):
        self.__contact_info = contact_info

    def __str__(self):
        """
        Returns a string representation of the customer with their details.
        """
        return "Customer(name='" + self.__name + "', contact_info='" + self.__contact_info + "')"

    # Method to update customer information
    def update_customer_info(self, name=None, contact_info=None):
        """Update customer details """
        if name:
            self.set_name(name)
        if contact_info:
            self.set_contact_info(contact_info)

    # Method to remove customer information 
    def remove_customer_info(self):
        """Remove customer information."""
        self.__name = None
        self.__contact_info = None
