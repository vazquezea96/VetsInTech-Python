# Week 1 - Day 3 Lesson: Booleans, Logic, and List

# Booleans
# In programming, we often need to check whether something is true or false. In Python,
# these values are represented by the Boolean type:
# - true
# - false

print(10 > 9) # True
print(10 == 9) # False
print(10 < 9) # False
# Each comparison returns either True or False.

# The bool() Function
# The built-in bool() function tells you whether a value is considered true or false
print(bool("Hello")) # True - non-empty string
print(bool(15)) # True - non-zero number

print(bool("")) # False - empty string
print(bool(0.0)) # False - zero
"""
General Rules:
- Non-empty strings, non-zero numbers, and non-empty objects -> True.
- Empty strings (""), zero (0, 0.0), and empty collections ([], {}, etc.) -> False.
"""

# Comparison Operators compare two values and return a Boolean result.
a = 4
b = 5
c = 5

print(a == b)  # False
print(b == c)  # True

print(a != b)  # True
print(b != c)  # False

print(a > b)   # False
print(b > c)   # False

print(a < b)   # True
print(b < c)   # False

print(a >= b)  # False
print(b >= c)  # True

print(a <= b)  # True

# Logical Operators combine Boolean expressions. They also return True or False.

# and Example
print(a > 2 and b == c) # True and True -> True

# or Example
print(a > 2 or b != c) # True or False -> True

# not Example
light_switch_on = True
opposite = not light_switch_on
print(opposite) # False

