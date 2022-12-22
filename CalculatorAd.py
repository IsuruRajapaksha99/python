

def addition(no_1,no_2):
    return no_1+no_2

def substraction(no_1,no_2):
    return no_1-no_2

def multiplication(no_1,no_2):
    return no_1*no_2

def division(no_1,no_2):
    return no_1/no_2

def power(no_1,no_2):
    return no_1**no_2

def remainder(no_1,no_2):
    return no_1%no_2


def s_op(choice):

    while (True):

        result
        if(choice== "+"):
            result = addition(num1,num2)

        elif(choice== "-"):
            result = substraction(num1,num2)

        elif(choice== "/"):
             result = division(num1,num2)

        elif(choice== "*"):
            result = multiplication(num1,num2)

        elif(choice== "**"):
            result = power(num1,num2)

        elif(choice== "%"):
            result = remainder(num1,num2)

        print(result)

while True:
    print (" Enter Operation ")
    print ("1. Add + ")
    print ("2. Substract - ")
    print ("3. Multiplication * ")
    print ("4. Division / ")
    print ("5. Power ** ")
    print ("6. Remainder % ")
    print ("7. History h ")

    
    choice= input(" Enter the operation +-*/**%h ")
    num1=float(input("Enter the first no "))
    num2=float(input("Enter the second no "))
    
    print(choice)
    s_op(choice)

    
    
    
