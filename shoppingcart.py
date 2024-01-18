from Item.items import Item
import csv
import os

# If you run shoppincart.py for the first time, this function creates the shopping_cart.csv file with field names.
def create_file():
    if "shopping_cart.csv" not in os.listdir("."):
        with open("shopping_cart.csv", "w") as cart:
                field_names = ["product_name", "price", "quantity", "sub_total"]
                csv_writer = csv.DictWriter(cart, fieldnames=field_names)
                csv_writer.writeheader()
# Function to append rows (without field name row) to the existing csv file.
def append_to_file():
     with open("shopping_cart.csv", "a") as cart:
        field_names = ["product_name", "price", "quantity", "sub_total"]
        csv_writer = csv.DictWriter(cart, fieldnames=field_names)
        for product in shoppin_cart:
             csv_writer.writerow(dict(
                  product_name=product["name"],
                  price=product["price"],
                  quantity=product["quantity"],
                  sub_total=product["sub_total"]
             ))
# To create product item.
def item_details(name: str, price: float, quantity: int):
    item = Item(name, price, quantity)
    return item
# This function checks if input can be changed into float.
def add_price():
        price = ""
        while True:
            price = input("Please enter price (decimal numbers can be used if needed):   ")
            try:
                if float(price):
                    break
            except ValueError as e:
                print("Please enter a number")
        return float(price)
# This function checks if input can be changed into integer.
def add_quantity():
        quantity = ""
        while True:
                quantity = input("Please enter quantity:    ")
                try:
                     if int(quantity):
                          break
                except ValueError as e:
                    print("Please enter a number")  
        return int(quantity)
#Shopping cart, and function to add to our shopping cart.
shoppin_cart = []
def add_to_cart(item):
    shoppin_cart.append(dict(name=item.name, price=item.price, quantity=item.quantity, sub_total=item.total_amount()))

# shoppingcart.py runs only as __main__.
if __name__ == "__main__":

    # While loop to add one or more items to our shopping cart.
    choice = ""
    while True:
        choice = input("Do you want to add to your cart? Y/N    ")
        if choice.lower() == 'y':
                name = input("Please enter product name:    ")
                price = add_price()
                quantity = add_quantity()
                product = item_details(name, price, quantity)
                add_to_cart(product)
        elif choice.lower() == "n":
                break
        else:
            print("Must be Y or N. Input is not case sensitive.")
    # In case of an empty cart shoppingcart.py won't create csv file.
    if len(shoppin_cart):
        create_file() 
        append_to_file()
        
    else:
        print("No product was added to your shopping cart")

