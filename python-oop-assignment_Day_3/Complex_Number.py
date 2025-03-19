class ComplexNumber:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary

    def __add__(self,other):
        #overload  + operator to add two  complex number
        return ComplexNumber(self.real+ other.real,self.imaginary+ other.imaginary)
    
    def __str__(self):
        #return String represent complex number
        return f"{self.real} +{self.imaginary}i "
    
c1=ComplexNumber(3,4)
c2=ComplexNumber(1,2)

c3=c1+c2  #uses overloaded + operator

print(c3)
        