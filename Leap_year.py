year=int(input("Enter a Year :")) #taken as input a year
if (year%400==0) or (year%4==0 and year%100!=0):# check condition for Leap year
    print("Given year is Leap Year: ",year) #if condition is True print Leap Year
else:
    print("Given Year is not Leap Year:",year) #if condition false print Not Leap year