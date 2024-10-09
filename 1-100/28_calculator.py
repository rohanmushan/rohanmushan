#Create a simple calculator that takes user input for two numbers and operation(+, -, *, /)
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
if(operation == '+'):
   sum=num1+num2
   print(f"sum of {num1} and {num2} is: {sum}")
elif(operation == '-'):
   sub=num1 - num2
   print(f"sub of {num1} and {num2} is: {sub}")
elif(operation == '*'):
   mul=num1 * num2
   print(f"mul of {num1} and {num2} is: {mul}")
elif(operation == '/'):
    if(num2!=0):
       div=num1/num2
       print(f"div of {num1} and {num2} is: {div}")
    else:
        print("Error: Division by zero")
else:
    print("Error: Invalid operation")
