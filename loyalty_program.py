class LoyaltyProgram:
    """
    Manages the loyalty program for customers. Applies a 10% discount for loyalty program members.
    """
    
    LOYALTY_DISCOUNT_RATE = 0.10  # 10% discount for members

    def __init__(self):
        self.__members = set()  # Set of customer names who are loyalty members

    def add_member(self, customer):
        """Add a customer to the loyalty program."""
        self.__members.add(customer.get_name())

    def is_member(self, customer):
        """Check if a customer is a loyalty program member."""
        return customer.get_name() in self.__members

    def get_discount_rate(self):
        return LoyaltyProgram.LOYALTY_DISCOUNT_RATE

    def __str__(self):
        members_list = ", ".join(self.__members)
        return "LoyaltyProgram(members=[" + members_list + "])"
