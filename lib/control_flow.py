# #!/usr/bin/env python3

# def admin_login(username, password):
#     # your code here
#     pass

# def hows_the_weather(temperature):
#     # your code here
#     pass

# def fizzbuzz(num):
#     # your code here
#     pass

# def calculator(operation, num1, num2):
#     # your code here
#     pass

def calculator(operation, num1, num2):
    if (operation == "+"):
        return num1 + num2
    elif (operation == "-"):
        return num1 - num
    elif (operation == "*"):
        return num1 * num
    elif (operation == "/"):
        if num2 != 0:
            return num1 / num2
        else: 
            print ("Invalid operation")
            
    else:
        return None
    
operation = input("Enter an operation (+,-,*,/) : ")
num1 = int(input("Enter Num1: "))
num2 = int(input("Enter Num2: "))

result = calculator(operation, num1, num2)
print(result)        
