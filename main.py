import re


# Converts a binary string to decimal
# Returns an error message if input is invalid
def binary_to_decimal(binary):
    if not re.fullmatch(r'[01]+', binary):
        return "Invalid binary input!"
    try:
        return int(binary, 2)  # Convert binary to decimal
    except ValueError:
        return "Invalid binary input!"


# Converts a decimal number to binary
# Returns an error message if input is invalid
def decimal_to_binary(decimal):
    try:
        decimal = int(decimal)  # Ensure input is an integer
        return bin(decimal).replace("0b", "")  # Convert decimal to binary
    except ValueError:
        return "Invalid decimal input!"


# Converts a binary string to hexadecimal
# Returns an error message if input is invalid
def binary_to_hex(binary):
    if not re.fullmatch(r'[01]+', binary):
        return "Invalid binary input!"
    try:
        return hex(int(binary, 2))[2:]  # Convert binary to hexadecimal
    except ValueError:
        return "Invalid binary input!"


# Converts a hexadecimal string to binary
# Returns an error message if input is invalid
def hex_to_binary(hexa):
    try:
        return bin(int(hexa, 16))[2:]  # Convert hexadecimal to binary
    except ValueError:
        return "Invalid hexadecimal input!"


# Converts a binary string to octal
# Returns an error message if input is invalid
def binary_to_octal(binary):
    if not re.fullmatch(r'[01]+', binary):
        return "Invalid binary input!"
    try:
        return oct(int(binary, 2))[2:]  # Convert binary to octal
    except ValueError:
        return "Invalid binary input!"


# Converts an octal string to binary
# Returns an error message if input is invalid
def octal_to_binary(octal):
    try:
        return bin(int(octal, 8))[2:]  # Convert octal to binary
    except ValueError:
        return "Invalid octal input!"


# Adds two binary numbers
# Returns an error message if inputs are invalid
def binary_addition(a, b):
    if not re.fullmatch(r'[01]+', a) or not re.fullmatch(r'[01]+', b):
        return "Invalid binary input!"
    try:
        return bin(int(a, 2) + int(b, 2))[2:]  # Perform binary addition
    except ValueError:
        return "Invalid binary input!"


# Subtracts two binary numbers
# Returns an error message if inputs are invalid
def binary_subtraction(a, b):
    if not re.fullmatch(r'[01]+', a) or not re.fullmatch(r'[01]+', b):
        return "Invalid binary input!"
    try:
        return bin(int(a, 2) - int(b, 2))[2:]  # Perform binary subtraction
    except ValueError:
        return "Invalid binary input!"


# Multiplies two binary numbers
# Returns an error message if inputs are invalid
def binary_multiplication(a, b):
    if not re.fullmatch(r'[01]+', a) or not re.fullmatch(r'[01]+', b):
        return "Invalid binary input!"
    try:
        return bin(int(a, 2) * int(b, 2))[2:]  # Perform binary multiplication
    except ValueError:
        return "Invalid binary input!"


# Divides two binary numbers
# Returns an error message if inputs are invalid or if division by zero occurs
def binary_division(a, b):
    if not re.fullmatch(r'[01]+', a) or not re.fullmatch(r'[01]+', b):
        return "Invalid binary input!"
    try:
        divisor = int(b, 2)
        if divisor == 0:
            return "Division by zero error!"
        return bin(int(a, 2) // divisor)[2:]  # Perform binary division
    except ValueError:
        return "Invalid binary input!"


# Main function to run the program
def main():
    print("Binary Conversion App")  # Display program title
    # Menu options
    print("1. Binary to Decimal")
    print("2. Decimal to Binary")
    print("3. Binary to Hexadecimal")
    print("4. Hexadecimal to Binary")
    print("5. Binary to Octal")
    print("6. Octal to Binary")
    print("7. Binary Addition")
    print("8. Binary Subtraction")
    print("9. Binary Multiplication")
    print("10. Binary Division")
    print("11. Exit")

    while True:
        choice = input("Choose an option (1-11): ")  # User input for menu choice

        # Perform actions based on user's choice
        if choice == '1':
            binary = input("Enter a binary number: ")
            print("Decimal:", binary_to_decimal(binary))

        elif choice == '2':
            decimal = input("Enter a decimal number: ")
            print("Binary:", decimal_to_binary(decimal))

        elif choice == '3':
            binary = input("Enter a binary number: ")
            print("Hexadecimal:", binary_to_hex(binary))

        elif choice == '4':
            hexa = input("Enter a hexadecimal number: ")
            print("Binary:", hex_to_binary(hexa))

        elif choice == '5':
            binary = input("Enter a binary number: ")
            print("Octal:", binary_to_octal(binary))

        elif choice == '6':
            octal = input("Enter an octal number: ")
            print("Binary:", octal_to_binary(octal))

        elif choice == '7':
            a = input("Enter first binary number: ")
            b = input("Enter second binary number: ")
            print("Addition:", binary_addition(a, b))

        elif choice == '8':
            a = input("Enter first binary number: ")
            b = input("Enter second binary number: ")
            print("Subtraction:", binary_subtraction(a, b))

        elif choice == '9':
            a = input("Enter first binary number: ")
            b = input("Enter second binary number: ")
            print("Multiplication:", binary_multiplication(a, b))

        elif choice == '10':
            a = input("Enter first binary number: ")
            b = input("Enter second binary number: ")
            print("Division:", binary_division(a, b))

        elif choice == '11':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice!")  # Handle invalid menu input


# Entry point of the program
if __name__ == "__main__":
    main()
