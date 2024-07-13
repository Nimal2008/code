class Item:
    pay_rate = 0.8 #pay after 20% discount and this is a class atribute
    def __init__(self,name: str,price: float,quantity: int):
        print("I am created")
        self.name = name
        self.price = price
        self.quantity = quantity
        assert price>=0, f"{price} is not greater than or equal to 0"
        assert quantity>=0,f"{quantity} is not greater than or equal to 0"
    def calculate_total_price(self):
        return(self.price*self.quantity)
    def calculate_discounted_price(self):
        return self.price*self.pay_rate






item1 = Item("Phone",100,5)
item2 = Item("Laptop",1000,3)
item3 =Item("PC",2500,7)
print(item1.calculate_total_price())
print(item2.calculate_total_price())
print(item1.__dict__)#all attributes for instance level(dictionary)
print(Item.__dict__)#attrivutes for class level
#print(Item.all)
