#Taken user input from all Three sides of Trangles
print("Enter All Side Of of Trangle")
Side_A=int(input("Enter Side A: "))
Side_B=int(input("Enter Side B: "))
Side_C=int(input("Enter Side C: "))

if Side_A==Side_B==Side_C:  # Check if codition for Equilateral Trangle
    print("Trangle Type Equilateral")
elif Side_A==Side_B or Side_A==Side_C or Side_C==Side_B: #check Condition for Isosceles
    print("Trangle Type Isosceles")
else:
    print("Trangle Type Scalence") #if above conditions are fail the default trangle ws Scalence