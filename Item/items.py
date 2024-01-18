#Item Class for shopping cart

class Item():
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total_amount(self):
        return "{:.2f}".format(self.quantity * self.price)
