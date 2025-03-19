import math
class Circle:
    default_radius=1 #default radius for Circle
    def __init__(self,radius=None):
        self.radius=radius if radius is not None else Circle.default_radius

    @classmethod
    def set_default_radius(cls,new_radius):
        cls.default_radius=new_radius

    @staticmethod
    def calculate_area(radius):
        return math.pi*radius*radius #calculate area of Circle
        
c1=Circle()
print(f"Radius :{c1.radius}, Area :{Circle.calculate_area(c1.radius)}")

c2=Circle(5) #given radius (5)
print(f"Radius :{c2.radius}, Area :{Circle.calculate_area(c2.radius)}")

Circle.set_default_radius(3) #set New Default Radius
c3=Circle()
print(f"Radius :{c3.radius}, Area :{Circle.calculate_area(c3.radius)}")


        

        
    