print("Hello")
name1 = input("Tell me your name ")
print(f"Hello {name1} this is a basic calculator that adds, subtracts, multiplies, and divides.")
number1 = float(input("Input a whole number "))
number2 = float(input("Input a second whole number "))
user_input = input("Would you lke to add , subtract , multiply or , divide?")
if user_input.lower() == 'add':
    print(f"your two numbers added together are {number1 + number2}")
elif user_input.lower() == 'subtract':
    print(f"your two numbers subtracted are {number1 - number2}")
elif user_input.lower() == 'multiply':
    print(f"your two numbers multiped are {number1 * number2}")
else:
    print(f"your two numbers divided are {number1 / number2}")   
          
#ask the user if they would like to do another number and allows them to use the program agin without running it again then asks of they are done then closes it
# print(f"The difference of ypu numbers is {number1 - number2}")
# print(f"The product of your number is {number1 * number2}")





