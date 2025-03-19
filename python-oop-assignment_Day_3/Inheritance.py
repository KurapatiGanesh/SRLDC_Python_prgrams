class vehical:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model 
class Car(vehical):
    def __init__(self, brand, model,fuel_type):
        super().__init__(brand, model)
        self.fuel_type=fuel_type
    
    def display(self):
        print(f"Brand: {self.brand}")
        print(f"Model :{self.model}")
        print(f"Fuel Type:{self.fuel_type}")
car1=Car("BMW","XPV","Petrol")
car1.display()
