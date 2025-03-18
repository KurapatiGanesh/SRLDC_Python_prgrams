#Taken user input as Number A, Number B and  Arithmatic Operators
Num_A=int(input("Enter Number A"))  
Num_B=int(input("Enter Number B:"))
symbol=input("Enter +,-,*,/ Symbol: ")

#check if condition for matching with operators 
if symbol=="+":
    print(" A + B=",Num_A+Num_B) # addition of two Number
elif symbol=="-":
    print("A - B =",Num_A-Num_B) #Substration of Two numbers
elif symbol=="*":
    print("A * B =",Num_A*Num_B) #Multiplication of two Number
elif symbol=="/":
    print("A / B =",Num_A/Num_B) #Division of Two Number
else:
    print("Invalid Symbol") # if symbol not matching in above coditions print invalid