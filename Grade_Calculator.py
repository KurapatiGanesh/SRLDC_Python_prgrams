#below Five subject taken as input
Operating_System=int(input("Enter Maths subject marks: "))
DBMS=int(input("Enter Maths subject marks: "))
java=int(input("Enter Maths subject marks: "))
data_structure=int(input("Enter Maths subject marks: "))
Machine_Learning=int(input("Enter Maths subject marks: "))
total=Operating_System+DBMS+java+data_structure+Machine_Learning
percentage=total/5
print("Percentage:",percentage)
if percentage>=90:
    print("Grade A")  #print Grade A if Percentage is Grater then 90

elif percentage>=80 and percentage<=89:
    print("Grade B") #print Grade B if Percentage in Between 80 to 89

elif percentage>=70 and percentage<=79:
    print("Grade C")  #print Grade B if Percentage in Between 70 to 79

elif percentage<70:  #print fail if perecentage is less than 70
    print("Fail")



