class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width 

    def area(self):
        return self.length*self.width
    
    def perimeter(self):
        return 2*(self.length+self.width)
    
rectangle1=Rectangle(10,20)
area_rect=rectangle1.area()
perimeter_Rect=rectangle1.perimeter()
print(f"area of rectangle: {area_rect}")
print(f"Rectangle Perimeter : {perimeter_Rect}")

        