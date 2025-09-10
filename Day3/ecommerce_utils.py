# E-commerce Billing System using Python modules.
# Create a module file named ecommerce_utils.py that contains the following functions:
# apply_discount(price, discount_percent) → applies a discount and returns the discounted price.
# add_gst(price, gst_percent=18) → adds GST (default 18%) and returns the new price.
# generate_invoice(cart, discount_percent=0, gst_percent=18) → accepts a dictionary cart (with product names as keys and prices as values) and prints a detailed invoice.
# Create a main program file named main.py that:
# Imports the ecommerce_utils module.
# Creates a shopping cart (dictionary) with at least 3 products.
# Calls the module functions to generate an invoice.
def apply_discount(price,discount_percent):
    return price-price*(discount_percent/100)
def add_gst(price,gst_percent=18):
    return price+price*(gst_percent/100)
def generate_invoice(cart, discount_percent=0, gst_percent=18):
    
    subTotal=sum(cart.values())
    print("ITEMS")
    for prod,price in cart.items():
        print(f"{prod} : {price}")
    
    print("SubTotal: ",subTotal)
    discounted_price = apply_discount(subTotal, discount_percent)
    final_price = add_gst(discounted_price, gst_percent)
    print(f"After {discount_percent}% discount the amount is: ",discounted_price)
    print("After 18% GST the amount to be paid is: ",add_gst(final_price))

        
     