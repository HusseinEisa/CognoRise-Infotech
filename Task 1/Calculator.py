# "CognoRise Infotech" Internship Task 1: create a calculator using python

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    # Check if the denominator is zero to avoid division by zero
    if y == 0:
        return "Error: Division by zero is not allowed."
    else:
        return x / y


##### Main program #####

# Display the welcome message
print("Welcome to the Calculator!")

# Infinite loop to keep the calculator running
while True:
    # Display the menu and get the user's choice
    print("\n","# "*40,"\n")
    print("Please select the operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    # Get the user's choice
    choice = input("Enter your choice (1-5): ")

    # If the user chooses to exit, display a goodbye message and exit the program
    if choice == '5':
        print("\nExiting the calculator. Goodbye!\n")
        exit()

    # Get the numbers from the user if the choice is between 1 and 4
    while (choice in ['1', '2', '3', '4']):
        try:
            # Get the first number from the user
            num1 = float(input("Enter the first number: "))
            # Get the second number from the user
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            # Display an error message if the user enters invalid input
            print("\nInvalid input. Please enter two numbers.\n")
            continue

    # Perform the selected operation and display the result
    if choice == '1':
        # Perform the addition operation and display the result
        print(f"\n{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        # Perform the subtraction operation and display the result
        print(f"\n{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        # Perform the multiplication operation and display the result
        print(f"\n{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        # Perform the division operation and display the result
        print(f"\n{num1} / {num2} = {divide(num1, num2)}")
    else:
        # Display an error message if the user enters invalid input
        print("\nInvalid input. Please enter a number between 1 and 5.\n")

