number1 = int(input("First number: "))
number2 = int(input("Second number: "))

operation = input("Operation [+, -, *, /]: ")

if operation == "+":
    combination = number1 + number2

elif operation == "-":
    combination = number1 - number2

elif operation == "*":
    combination = number1 * number2

elif operation == "/":
    if number2 == 0:
        combination= "you can’t divide by zero."
    else:
        combination = number1 / number2

else:
    combination = "ERROR ... '" + operation + "' unrecognised"

print("Answer: " + str(combination))

print()
input("Press return to continue ...")
