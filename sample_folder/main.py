import math

print("Hello, world!")
print(42)
print("The answer is", 42)
print('hello')
print("Python")
print("That's my favorite book")
print('He said "What is your name?"')

print("Line 1\nLine 2\nLine 3")
print("""This is line 1.
This is line 2.
This is line 3.""")
# This is a comment line.
# Python skips this when executing.

print("This will run.") # This is an inline comment.

my_variable = "a string"
age = 29
pi = 3.14

# valid exmples
my_name = "Jael"
_name = "Andre"
name1 = "Student"

# invalid examples:
# 1name = "error" # starts with a number 
# my-name = "error" # contains a hypen

# Multi-world variable names
MyFavoriteBand = "Pierce the Veil" # PascalCase
myFavoriteFood = "Pizza" # camelCase
my_favorite_programming_language = "Python" # snake_case preferred in Python

# Printing variables
name = "Eddie"
print(name)

# User Input with input()
""" The input() function lets your program receive information from the user.
It shows a prompt, waits for the user to type something, and then returns that text as string.  """

# user_age = input("What is your age? ")
# print("Wow, you look good for " + user_age)

# Topics for Day 2 

# Python tracks the type of each value (for example: text vs number).
# You'll learn to use type() to inspect a value and understand how
# Python sees it.

# Variables
# - Casting: turing one type into another (e.g., "42" -> 42).
# - Using type(): checking what kind of data a variable holds.

# Numbers in Python
# three numeric types:
# int - integers (whole numbers), e.g., 3, -10, 42
# float - decimal numbers, e.g., 3.14, -0.5, 2.0
# complex - complex numbers, e.g., 3+4j (advanced / "strech" concept)

# Arithmetic Operators
# You'll use Python as a calculator and learn the core arithmetic operators:
# + (addition), - (subtraction)
# (*) (multiplication), / (division)
# (//) (floor division), % (modulus / remainder)
# (**)(exponentiation)

hours = 5
rate = 45
pay = hours * rate

# 1 Data Types
"""
In programming, a data type defines the kind of value a variable can hold
and what operations you can perform with it.
Python comes with several built-in data types, organized into categories:
- Text Types: str
- Numeric Types: int, float, complex
- Boolean Type: bool
- Sequence Types: list, tuple, range
- Mapping Type: dict
- Set Types: set, frozenset
- Binary Types: bytes, bytearray, memoryview
"""

# 2. Variables and Data Types (continuation)

str_example = "Hello World" # str
int_example = 20 # int
float_example = 20.5 # float
bool_example = True # bool
list_example = ["apple", "banana", "cherry"] # list
range_example = range(6) # range
dict_example = {"name": "John", "age": 36} # dict
complex_example = 2 + 3j # complex
tuple_example = ("apple", "banana", "cherry") # tuple
set_example = {"apple", "banana", "cherry"} # set
frozenset_example = frozenset({"apple", "banana", "cherry"}) # frozenset
byte_example = b"Hello" # bytes
bytearray_example = bytearray(5) # bytearray
memoryview_example = memoryview(bytes(5)) # memoryview

print(type(str_example))
print(type(int_example))

# 3. Numbers 
# Python has three generic types:
# - int: Whole numbers, positive or negative, without decimals
x = 42
y = -10
z = 12345678901234567890 # Python can handle big intetgers

# Floating Point Numbers
# - float : Numbers with decimals, positive or negative
pi = 3.14159
temperature = -12.5

print(pi, type(pi))
print(temperature, type(temperature))
# Complex Numbers

z1 = 2 + 3j
print(z1, type(z1))

# 4. Arithmetic Operators
# Python uses these operatirs to do basic math:
# (+) Addition (x + y)
# (-) Subtraction (x - y)
# (*) Multiplication (x * y)
# (/) Division (x / y)
# (//) Floor Division (x // y)
# (%) Modulus (x % y)
# (**) Exponentiation (x ** y)

# Using Variables with Operators
# Addition
sum_result = 4 + 4
print(sum_result)

# Subtraction (can givve negatives)
sub_result = 1 - 100
print(sub_result)

# Division (return a float)
div_result = 10 / 5
print(div_result)

# Floor division (drops the decimal part)
floor_result = 10 // 3
print(floor_result)

# Modulus (remainder after division)
remainder = 10 % 3
print(remainder)

# Exponentiation (power)
power = 2 ** 5
print(power)

# Modules and Functions
"""
A module in Python is a like a code library - a file that contains functions you can reuse. Modules save you from having to write the same code over and over again.

Python gives you:
- Built-in functions like print(), input(), type()
- The standard library - a collection of modules you can import when needed.
"""

# The round() Function
# Python includes a built-in function called round() that rounds numbers.
# It takes one required argument (the number) and an optional second
# argument.

number = 1.23456
print(round(number)) # 1 -> rounded to 0 digits (int)
print(round(number, 0)) # 1.0 -> 0 digits, returns float
print(round(number, 1)) # 1.2 -> 1 decimal place
print(round(number, 2)) # 1.23 -> 2 decimal place
print(round(number, 3)) # 1.235 -> 3 decimal places (last digit rounded up)
# round() sometimes rounds up and sometimes down, depending on the last digit.

# Importing Modules: math.ceil()
# if you alwyas want to round up, you can use the math module's ceil() function
num = 4.3
print(math.ceil(num)) # 5

# Updating Variables and Assignment Operators
# Updating a Variable

x1 = 10
x1 = x + 5 # update the existing variable
print(x1)

# Assignment Operators let us combine assignment and arithmetic in shorthand form
x1 += 5
print(x1)

"""
8. Casting (Changing Data Types)
What is Casting?
Casting means changing the type of data so Python can use it the way you want.
- You can't add a string "5" to a number 5 without converting one of them.
- Python uses special functions called constructors to do this: int(), float(), str(), etc.
"""

# int() -> Convert to Integer (Whole Numbers)
# The int() function turns something into a whole number.
# From an integer (stays the same)
a = int(1)
print(a) # 1

# From a float (decimal part is dropped, not rounded)
b = int(12.9)
print(b) # 12

# From a string (if the string is a whole number)
c = int("15")
print(c) # 15

# float() -> Convert to Decimal Numbers
# The float() function turns value into numbers with decimals

# From an integer
e = float(12)
print(e)   # 12.0

# From a float (stays the same)
f = float(12.5)
print(f)   # 12.5

# From a string that looks like a number
g = float("100")
print(g)   # 100.0

string_number = "12554.34"
print(float(string_number))  # 12554.34

# Example: casting a string with decimals:
num_str = "12.5"

# This will cause an error:
# print(int(num_str))

# First convert to float, then to int
num_float = float(num_str)  # 12.5
num_int = int(num_float)    # 12

print("As float:", num_float)
print("As int:", num_int)

# str() Convert to string(text)
# The str() function turns almost anything into text

# From a string (no change)
h = str("hello")
print(h)

# From an integer
i = str(1)
print(i)   # "1"

# From a float
j = str(1230.45)
print(j)

# Use str() when you need to display values in messages or build text output.

# 9. F-Strings: The Easy Way to Mix Text and Variables
"""
What's an F-String?
- An f-string is a string that starts with f before the opening quote. Inside the string, 
you can put variables directly in curly braces {} - Python automatically converts them to
text for you.
"""
# Without f-strings (clunky)
print("My name is " + name + " and I am " + str(age) + " years old.")

# With f-strings (clean)
print(f"My name is {name} and I am {age} years old.")

price = 19.99
quantity = 3

print(f"Total: ${price * quantity}")

# Formatting Numbers
# F-strings also let you control how numbers are displayed:
pi = 3.14159265359

# Round to 2 decimal places
print(f"Pi is approximately {pi:.2f}")
# Output: Pi is approximately 3.14

# Add commas to big numbers
big_number = 1000000
print(f"One million: {big_number:,}")
# Output: One million: 1,000,000

# 10. Example: User Input and Casting
# Ask the user for their age
age = input("Enter your age: ")
print(type(age))   # <class 'str'>

# Cast to integer so we can add to it
age = int(age)
print(f"Next year, you will be {age + 1}")
