from loyalty_program import LoyaltyProgram

class Invoice:
    """
    Generates an invoice detailing item prices, discounts, VAT, and the final amount.
    """
    
    VAT_RATE = 0.08  # Fixed VAT rate of 8%
    BULK_DISCOUNT_RATE = 0.20  # 20% discount for bulk purchases (5+ e-books)

    def __init__(self, order, loyalty_program):
        self.__order = order
        self.__loyalty_program = loyalty_program

    def calculate_total(self):
        """Calculates the total price with VAT, loyalty, and bulk discounts."""
        cart = self.__order.get_cart()
        subtotal = sum(item.get_price() * quantity for item, quantity in cart.get_items().items())
        discount = 0

        # Apply loyalty discount
        if self.__loyalty_program.is_member(self.__order.get_customer()):
            discount += LoyaltyProgram.LOYALTY_DISCOUNT_RATE * subtotal

        # Apply bulk discount
        if cart.get_total_items() >= 5:
            discount += Invoice.BULK_DISCOUNT_RATE * subtotal

        vat = (subtotal - discount) * Invoice.VAT_RATE
        total = subtotal - discount + vat

        return {"subtotal": subtotal, "discount": discount, "vat": vat, "total": total}

    def __str__(self):
        total_details = self.calculate_total()
        return ("Invoice(subtotal=" + str(total_details["subtotal"]) +
                ", discount=" + str(total_details["discount"]) +
                ", VAT=" + str(total_details["vat"]) +
                ", total=" + str(total_details["total"]) + ")")
