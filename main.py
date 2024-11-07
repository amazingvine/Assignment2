from ebook import EBook
from catalog import Catalog
from customer import Customer
from loyalty_program import LoyaltyProgram
from shopping_cart import ShoppingCart
from order import Order
from invoice import Invoice
from payment import Payment

def main():
    # Creating e-books with Arabic names in English transliteration
    ebook1 = EBook("Programming Fund", "Ali Al-Ahmad", "2023-01-15", "Technology", 25.00)
    ebook2 = EBook("Basics of Python", "Maryam Khaled", "2022-06-10", "Data Science", 30.00)
    ebook3 = EBook("Basics of C++", "Sarah Hussein", "2021-03-22", "History", 15.00)
    ebook4 = EBook("Calculus", "Ahmed Mustafa", "2020-09-12", "Economics", 20.00)
    ebook5 = EBook("Machine Learning", "Noor Al-Din Muhammad", "2019-11-05", "Science", 18.00)
    ebook6 = EBook("Data Structures", "Fatima Al-Muntheri", "2023-07-10", "Linguistics", 22.00)
    ebook7 = EBook("Algorithm", "Youssef Saeed", "2021-02-18", "Philosophy", 28.00)
    ebook8 = EBook("Physics", "Layla Hassan", "2018-08-30", "Literature", 19.00)
    
    # Adding e-books to the catalog
    catalog = Catalog()
    catalog.add_ebook(ebook1)
    catalog.add_ebook(ebook2)
    catalog.add_ebook(ebook3)
    catalog.add_ebook(ebook4)
    catalog.add_ebook(ebook5)
    catalog.add_ebook(ebook6)
    catalog.add_ebook(ebook7)
    catalog.add_ebook(ebook8)
    
    # Creating a customer
    customer = Customer("Saeed Youssef", "saeed@gmail.com")
    print(customer)

    # Loyalty program
    loyalty_program = LoyaltyProgram()
    loyalty_program.add_member(customer)
    
    # Shopping cart
    cart = ShoppingCart()
    cart.add_ebook(ebook1, 2)
    cart.add_ebook(ebook2, 3)
    cart.add_ebook(ebook3)
    cart.add_ebook(ebook5)
    print(cart.display_cart_items())
    
    # Creating an order and generating an invoice
    order = Order(customer, cart)
    invoice = Invoice(order, loyalty_program)
    print(invoice)
    
    # Processing payment
    payment = Payment(invoice.calculate_total()["total"])
    print(payment.process_payment())

if __name__ == "__main__":
    main()
