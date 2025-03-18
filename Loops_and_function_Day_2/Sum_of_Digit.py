
def sum_of_digit(number):
    sum=0
    while(number>0):
        
        digit=number%10 #extract last digit from Number
        sum=sum+digit #add to Sum of Number
        number=number//10 # remove last digit of Number
    return sum
    

number=int(input("Enter A Number:"))
print(sum_of_digit(number)) # funcation call
