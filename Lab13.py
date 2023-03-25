# Creating a string
my_string = "Hello, World!"

# Accessing individual characters
print(my_string[0])   # Output: "H"
print(my_string[-1])   # Output: "!"

# Concatenating strings
greeting = "Hello"
name = "Alice"
message = greeting + ", " + name + "!"
print(message)   # Output: "Hello, Alice!"

# Repeating a string
my_string = "Hello"
repeated_string = my_string * 3
print(repeated_string)   # Output: "HelloHelloHello"

# Converting a string to uppercase
my_string = "Hello, World!"
print(my_string.upper())   # Output: "HELLO, WORLD!"

# Converting a string to lowercase
my_string = "Hello, World!"
print(my_string.lower())   # Output: "hello, world!"

# Checking if a substring is in a string
my_string = "Hello, World!"
print("World" in my_string)   # Output: True
print("Alice" in my_string)   # Output: False

# Splitting a string into a list of substrings
my_string = "Hello, World!"
print(my_string.split(","))   # Output: ["Hello", " World!"]

# Replacing a substring with another substring
my_string = "Hello, World!"
print(my_string.replace("Hello", "Goodbye"))   # Output: "Goodbye, World!"
