# Ask user to enter a number
number = int(input("Enter a number: "))

# Check if the number is positive, negative or zero
if number > 0:
    print("The number is positive")
elif number == 0:
    print("The number is zero")
else:
    print("The number is negative")
