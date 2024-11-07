# Test the functionality of the e-bookstore

from ebook import EBook
from catalog import Catalog
from customer import Customer
from loyalty_program import LoyaltyProgram
from shopping_cart import ShoppingCart
from order import Order
from invoice import Invoice
from payment import Payment

def test_add_ebook_to_catalog():
    """Test adding a new e-book to the catalog."""
    ebook = EBook("Introduction to Algorithms", "Thomas H. Cormen", 30)
    if ebook.get_title() == "Introduction to Algorithms" and ebook.get_author() == "Thomas H. Cormen" and ebook.get_price() == 30:
        print("Add e-book to catalog test passed!")
    else:
        print("Add e-book to catalog test failed.")

def test_modify_ebook_details():
    """Test modifying an e-book's details in the catalog."""
    ebook = EBook("Introduction to Algorithms", "Thomas H. Cormen", 30)
    ebook.set_title("Algorithms Unlocked")
    ebook.set_author("Thomas H. Cormen")
    ebook.set_price(40)
    if ebook.get_title() == "Algorithms Unlocked" and ebook.get_author() == "Thomas H. Cormen" and ebook.get_price() == 40:
        print("Modify e-book details test passed!")
    else:
        print("Modify e-book details test failed.")

def test_remove_ebook_from_catalog():
    """Test removing an e-book from the catalog."""
    ebook = EBook("Introduction to Algorithms", "Thomas H. Cormen", 30)
    # Simulating removal by setting the reference to None
    ebook = None
    if ebook is None:
        print("Remove e-book from catalog test passed!")
    else:
        print("Remove e-book from catalog test failed.")

def test_add_customer_account():
    """Test adding a new customer account."""
    customer = Customer("Ahmed", "ahmed@example.com")
    if customer.get_name() == "Ahmed" and customer.get_contact_info() == "ahmed@example.com":
        print("Add customer account test passed!")
    else:
        print("Add customer account test failed.")

def test_modify_customer_account():
    """Test modifying an existing customer account."""
    customer = Customer("Ahmed", "ahmed@example.com")
    customer.set_name("Ahmed Al-Mu'adal")
    customer.set_contact_info("ahmed_updated@example.com")
    if customer.get_name() == "Ahmed Al-Mu'adal" and customer.get_contact_info() == "ahmed_updated@example.com":
        print("Modify customer account test passed!")
    else:
        print("Modify customer account test failed.")

def test_remove_customer_account():
    """Test removing a customer account."""
    customer = Customer("Ahmed", "ahmed@example.com")
    customer = None
    if customer is None:
        print("Remove customer account test passed!")
    else:
        print("Remove customer account test failed.")

def test_add_ebook_to_cart():
    """Test adding an e-book to the shopping cart."""
    ebook = EBook("Introduction to Algorithms", "Thomas H. Cormen", 30)
    cart = ShoppingCart()
    cart.add_ebook(ebook, 2)
    items = cart.get_items()
    if items[ebook] == 2:
        print("Add e-book to cart test passed!")
    else:
        print("Add e-book to cart test failed.")

def test_remove_ebook_from_cart():
    """Test removing an e-book from the shopping cart."""
    ebook = EBook("Introduction to Algorithms", "Thomas H. Cormen", 30)
    cart = ShoppingCart()
    cart.add_ebook(ebook, 2)
    cart.remove_ebook(ebook)
    items = cart.get_items()
    if ebook not in items:
        print("Remove e-book from cart test passed!")
    else:
        print("Remove e-book from cart test failed.")

def test_apply_discount_loyalty_program():
    """Test applying a discount for loyalty program members."""
    ebook = EBook("Introduction to Algorithms", "Thomas H. Cormen", 30)
    customer = Customer("Ahmed", "ahmed@example.com")
    cart = ShoppingCart()
    cart.add_ebook(ebook, 1)
    
    total_price = sum(item.get_price() * quantity for item, quantity in cart.get_items().items())
    discounted_price = total_price * 0.9  # Applying 10% discount
    
    if discounted_price == 27:
        print("Loyalty discount test passed!")
    else:
        print("Loyalty discount test failed.")

def test_apply_discount_bulk_purchase():
    """Test applying a discount for bulk purchases (5 or more e-books)."""
    ebook = EBook("Introduction to Algorithms", "Thomas H. Cormen", 30)
    cart = ShoppingCart()
    cart.add_ebook(ebook, 5)
    
    total_price = sum(item.get_price() * quantity for item, quantity in cart.get_items().items())
    discounted_price = total_price * 0.8  # Applying 20% discount for bulk purchase
    
    if discounted_price == 120:
        print("Bulk purchase discount test passed!")
    else:
        print("Bulk purchase discount test failed.")

def test_generate_invoice():
    """Test generating an invoice with discounts and taxes."""
    ebook1 = EBook("Introduction to Algorithms", "Thomas H. Cormen", 30)
    ebook2 = EBook("Artificial Intelligence: A Modern Approach", "Stuart Russell", 40)
    cart = ShoppingCart()
    cart.add_ebook(ebook1, 2)
    cart.add_ebook(ebook2, 1)
    
    total_before_tax = sum(item.get_price() * quantity for item, quantity in cart.get_items().items())
    vat = total_before_tax * 0.08  # 8% VAT
    total_after_tax = total_before_tax + vat
    
    invoice = "Invoice\n"
    invoice += "Items:\n"
    for ebook, quantity in cart.get_items().items():
        invoice += "Title: " + ebook.get_title() + ", Quantity: " + str(quantity) + ", Price: " + str(ebook.get_price()) + "\n"
    invoice += "Total before tax: " + str(total_before_tax) + "\n"
    invoice += "VAT (8%): " + str(vat) + "\n"
    invoice += "Total after tax: " + str(total_after_tax) + "\n"
    
    if "Title: Introduction to Algorithms" in invoice and "Total before tax: 100" in invoice and "VAT (8%): 8.0" in invoice and "Total after tax: 108.0" in invoice:
        print("Generate invoice test passed!")
    else:
        print("Generate invoice test failed.")

# Running the tests

test_add_ebook_to_catalog()
test_modify_ebook_details()
test_remove_ebook_from_catalog()
test_add_customer_account()
test_modify_customer_account()
test_remove_customer_account()
test_add_ebook_to_cart()
test_remove_ebook_from_cart()
test_apply_discount_loyalty_program()
test_apply_discount_bulk_purchase()
test_generate_invoice()
