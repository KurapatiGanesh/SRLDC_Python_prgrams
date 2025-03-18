def Factorial(number):
    result=1
    for i in range(1,number+1):
        result=result*i #multifly result by current number
    return result
number=int(input("Enter a Number: "))
print(Factorial(number))
