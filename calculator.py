num1 = float(input("Enter the First number"))
operator = input("Enter the operator (+, -, *, /):")
num2 = float(input("Enter the Second number"))

if operator == "+":
    print('Result: ', num1+num2)
elif operator == "-":
    print('Result: ', num1-num2)
elif operator == "*":
    print('Result: ', num1*num2)
elif operator == "/":
    print('Result: ', num1/num2)
    if num2 == 0:
        print('Result: ', num1/num2)
    else :
        print('cannot divided by zero')
else:
    print('Invalid operator')


    
        
    

