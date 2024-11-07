class Payment:
    """
    Handles payment for an order.
    """
    
    def __init__(self, amount):
        self.__amount = amount

    def process_payment(self):
        """Processes the payment."""
        return "Payment of amount " + str(self.__amount) + " processed successfully."

    def __str__(self):
        return "Payment(amount=" + str(self.__amount) + ")"
