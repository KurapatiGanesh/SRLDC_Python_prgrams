
def fabonacci(num):
    a=0
    b=1
    for i in range(0,num): #put Nth number in Loop
        print(a)      #display fabonacci series through iteration
        a,b=b,a+b #swap a=b and b=a+b
              
num=int(input("Enter A number: "))

fabonacci(num) #function call