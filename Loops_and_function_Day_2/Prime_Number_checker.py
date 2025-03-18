def prime(number):
    if(number<2):
        return False
    for i in range(2,(number//2)+1):
        if number%i==0:
            return False
    return True
    
number=int(input("Enter A Number: "))
if prime(number)==True:
    print("Number is Prime Number")
else:
    print("Number is Not Prime Number")