class Employee:
    def __init__(self,name,id,basic_salary):
        self.name=name
        self.id=id
        self.basic_salary=basic_salary

    def Cal_gross_salary(self):
        hra=0.10* self.basic_salary
        da=0.05 *self.basic_salary
        gross_salary=self.basic_salary+hra+da
        return gross_salary
    
    def display_details(self):
        print(f" Employee Name: {self.name}")
        print(f"Employee Id : {self.id}")
        print(f"Employee basic Salary:{self.basic_salary}")
        print(f"Employee Gross salary :{self.Cal_gross_salary()}")

emp=Employee("Ganesh Kurapati",10,15000)
emp.display_details()
