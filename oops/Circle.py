class Circle():
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    @property
    def Area(self):
        return self.pi*self.radius*self.radius
    
c1=Circle(7)
#c1.radius=8
print(c1.Area)
