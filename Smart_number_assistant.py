import math

# Function to check if a number is even or odd.
def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is a even number."
    else:
        return f"{number} is a odd number."
    
# function to check number is prime or composite.
    
def check_prime(number):
    if number <= 1:
        return f"{number} is not a prime number."
    for i in range(2, int(number ** 0.5)+1):
        if number % i == 0 :
            return f"{number} is a composite number."
    else:
        return f"{number} is a prime number."
        
# function to calculate square of a number.

def calc_square(number):
    return f"Sqaure of {number} is {number ** 2}."

#function to calculate cube of a number.

def calc_cube(number):
    return f"Cube of {number} is {number ** 3}."

# function to calculate square root of a number.

def calc_square_root(number):
    if number < 0:
        return "Cannot calculate sqaure root of a negative number."
    return f"Sqaure root of {number} is {number ** 0.5:.2f}."

# function to calculate factorial of a number.

def calculate_factorial(number):
    if number < 0:
        return "Factorial is not calculated for negative number."
    return f"The factorial of {number} is {math.factorial(number)}"

# function to check if the number is palindrome.

def check_palindrome(number):
    if str(number) == str(number) [::-1]:
        return f"{number} is a palindrome number."
    else:
        return f"{number} is not a palindrome number."
    

# function to check if the number is armstrong number.

def check_armstrong(number):
    num_str = str(number)
    power = len(num_str)
    total = sum(int(digit) ** power for digit in num_str)
    if total == number:
        return f"{number} is an armstrong number."
    return f"{number} is not an armstrong number."

# Function to list all factors

def list_factors(number):
    factors = [i for i in range (1, number+1) if number % i ==0]
    return f"Factors of {number} are: {factors}"

# Function to check perfect number

def check_perfect_number(number):
    divisors = [i for i in range(1, number) if number % i == 0]
    if sum(divisors) == number:
        return f"{number} is a perfect number."
    return f"{number} is not a perfect number."

# function to show multiplication table.

def show_multiplication_table(number):
    print(f"\n Multiplication table of {number}")
    for i in range(1, 11):
        print(f"{number} X {i} = {number * i}")

# Function to convert to binary, octal, hex

def convert_bases(number):
    return f"Binary : {bin(number)}, Octal : {oct(number)}, Hexadecimal : {hex(number)}"


# Interacts with user.

def main():
    print("Welcome to Apoorv's Smart Number Assistant!")

    while True:
        user_input = input("Please enter a number (or type 'exit' to quit.): ")

        if user_input.lower() == 'exit':
            print("Exiting the assistant. Goodbye!")
            break

        if not user_input.isdigit():
            print("Invalid input. Please enter a valid positive integer.")
            continue

        number = int(user_input)

        while True:
            print(f"\n📋 MENU - What would you like to check for {number}?")
            print("1. Check Even/Odd")
            print("2. Check Prime/Composite")
            print("3. Check Palindrome")
            print("4. Check Armstrong Number")
            print("5. Check Perfect Number")
            print("6. Calculate Sqaure, Cube, Square Root")
            print("7. Calculate Factorial")
            print("8. List Factors")
            print("9. Show Multiplication Table")
            print("10. Convert Number System(Binary, Octal, Hex)")
            print("11. Enter a New Number")
            print("0. Exit the Assistant")

            choice = input("👉 Enter your choice (0-11): ")

            if choice == "1":
                print(check_even_odd(number))
            elif choice == "2":
                print(check_prime(number))
            elif choice == "3":
                print(check_palindrome(number))
            elif choice == "4":
                print(check_armstrong(number))
            elif choice == "5":
                print(check_perfect_number(number))
            elif choice == "6":
                print(calc_square(number))
                print(calc_cube(number))
                print(calc_square_root(number))
            elif choice == "7":
                print(calculate_factorial(number))
            elif choice == "8":
                print(list_factors(number))
            elif choice == "9":
                print(show_multiplication_table(number))
            elif choice == "10":
                print(convert_bases(number))
            elif choice == '11':
                break
            elif choice == "0":
                print("Exiting the Assistant. Goodbye!")
                return
            else:
                print("❌ Invalid choice. Please enter a number between 0 and 11.")


if __name__ == "__main__":
    main()








