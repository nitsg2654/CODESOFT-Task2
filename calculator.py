def calculator():
    print("Simple Calculator")
    
    #Prompt user for the first number
    num1 = float(input("Enter the first number: "))
    
    #Prompt user for the second number
    num2 = float(input("Enter the second number: "))
    
    #Displaying operation choices
    print("\nChoose the operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    #Prompting user for the operation choice
    operation = input("Enter the operation (1/2/3/4): ")
    
    #Performing the calculation and display the result
    if operation == '1':
        result = num1 + num2
        print("\nThe result of", num1 + num2, "is: ", result)
    elif operation == '2':
        result = num1 - num2
        print("\nThe result of", num1 - num2, "is: ", result)
    elif operation == '3':
        result = num1 * num2
        print("\nThe result of", num1 * num2, "is:", result)
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print("\nThe result of ", num1 / num2, "is: ", result)
        else:
            print("\nError: Division by zero is not allowed.")
    else:
        print("\nInvalid operation choice. Please try again.")

#Run the calculator function
calculator()
