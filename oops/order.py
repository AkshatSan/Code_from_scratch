class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,ord2):
        return self.price>ord2.price
ord1=Order("pizza",50)
ord2=Order("pasta",60)
print(ord1>ord2)