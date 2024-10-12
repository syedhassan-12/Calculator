num1 = int(input("What is your first number?"))
num2 = int(input("What is your second number?"))
operation = int(input("What operation do you want to apply?\n 1)Addition \n 2)Subtraction \n 3)Multiplication \n 4)Divide \n Enter Operation: "))

if operation == 1:
    print(num1 + num2)
elif operation == 2:
    print(num1 - num2)
elif operation == 3:
    print("num1 * num2")
elif operation == 4:
    print(num1/num2)
else:
    print("Sorry we cannot apply this operation")
