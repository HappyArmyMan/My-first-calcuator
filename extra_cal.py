print("Hello")
name1 = input("Tell me your name ")
print(f"hello {name1}, this is a basic calculator that adds, subtracts, multiplies, and divides.")
while True:    
    number1 = float(input("Input a whole number "))
    number2 = float(input("Input a second whole number "))
    user_input = input("Would you like to add, subtract, multiply, or divide? ")
    if user_input.lower() == 'add':
        print(f"Your two numbers added together are {number1 + number2}")
    elif user_input.lower().startswith('sub'):
        print(f"Your two numbers subtracted are {number1 - number2}")
    elif user_input.lower().startswith('mul'):
        print(f"Your two numbers multiplied are {number1 * number2}")
    elif user_input.lower().startswith('div'):
        print(f"Your two numbers divided are {number1 / number2}")
    else:
        print("Thats not an option dummy try again ")
        continue
    another_calculation = input("Would you like to perform another calculation? (yes/no) ")
    if another_calculation.lower() == 'yes':
        continue
    else:
        print("Thank you for using this calculator.")
        break