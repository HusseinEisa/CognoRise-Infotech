import random
from math import ceil

# Generate the letters for the password
def Letters(Letters_length):
    Small_letters = ""  # create an empty string to store the small letters
    Big_letters = ""  # create an empty string to store the big letters

    # Generate the small letters
    for i in range(ceil(Letters_length / 2)):
        Big_letters += chr(random.randint(65, 90))
    
    # Generate the big letters
    for i in range(Letters_length - ceil(Letters_length / 2)):
        Small_letters += chr(random.randint(97, 122))
    
    # Return small and big letters as concatenation
    return Small_letters + Big_letters

# Generate the numbers for the password
def Numbers(Numbers_length):
    Numbers = ""  # create an empty string to store the numbers
    
    # Generate the numbers
    for i in range(Numbers_length):
        Numbers += str(random.randint(0, 9))
    
    # Return the numbers
    return Numbers

# Generate the symbols for the password
def Symbols(Symbols_length):
    All_Symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"  # create a string of all symbols
    Symbols = ""  # create an empty string to store the symbols of password
    
    # Generate the symbols
    for i in range(Symbols_length):
        Symbols += random.choice(All_Symbols)
    
    # Return the symbols
    return Symbols

# Generate the password
def Password_Generator(Password_Length):
    Password = ""  # create an empty string to store the password
    
    # calculate the length of the letters and make it equal to 60% of the password length
    Letters_length = ceil(Password_Length * 0.6)
    
    # calculate the length of the numbers and make it equal to 30% of the password length
    Numbers_length = ceil(Password_Length * 0.3)
    
    # calculate the length of the symbols and make it equal to the remaining 10% of the password length
    Symbols_length = Password_Length - (Letters_length + Numbers_length)

    # Generate the letters and add them to the password
    Password += Letters(Letters_length)
    
    # Generate the numbers and add them to the password
    Password += Numbers(Numbers_length)
    
    # Generate the symbols and add them to the password
    Password += Symbols(Symbols_length)

    # convert the password to a list and shuffle it
    Password = list(Password)
    random.shuffle(Password)
    
    # re-convert the password to a string
    Password = "".join(Password)
    
    # Return the password
    return Password


##### Main program #####

# Display the welcome message
print("\nWelcome to the Password Generator!")

# Infinite loop to keep the program running
while True:
    # Display the menu and get the user's choice
    print("\n","# "*40,"\n")
    print("1. Generate a password")
    print("2. Exit")

    # Get the user's choice
    choice = input("Enter your choice (1-2): ")

    # If the user chooses to exit, display a goodbye message and exit the program
    if choice == '2':
        print("\nExiting... Goodbye!\n")
        exit()

    # Get the numbers from the user if the choice is between 1 and 4
    while (choice == '1'):
        try:
            # Get the length of the password
            Password_Length = int(input("Enter the length of the password: "))
            break
        except ValueError:
            # Display an error message if the user enters invalid input
            print("\nInvalid input. Please enter an integer number.\n")
            continue
    
    if choice == "1":
        # Display the password
        print("\nYour password is: ", end="")
        # Generate the password and display it
        print(Password_Generator(Password_Length))
    else:
        # Display an error message if the user enters invalid input
        print("\nInvalid input. Please enter a number 1 or 2.\n")