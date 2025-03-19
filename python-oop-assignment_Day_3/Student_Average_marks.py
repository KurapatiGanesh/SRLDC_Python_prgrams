class Student:
    def __init__(self,name,roll_number,marks):
        self.name=name
        self.roll_number=roll_number
        self.marks=marks
    def calculate_avg(self):
        if len(self.marks)>0:
            return sum(self.marks)/len(self.marks)
        else:
            return 0
student1=Student("Ganesh Kurapati",18,[78,67,98,67,54])
avg_marks=student1.calculate_avg()
print(f"{student1.name} Avarage Marks is: {avg_marks}")
        