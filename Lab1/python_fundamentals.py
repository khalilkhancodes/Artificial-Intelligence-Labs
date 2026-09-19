# Lab 1: Python Fundamentals
# This file covers indentation, reserved words, and data types

print("=" * 60)
print("PART 1: INDENTATION")
print("=" * 60)

# Python uses indentation to define code blocks
# Unlike C/C++ which use braces {}

# Basic indentation with if statement
x = 10
if x > 5:
    print("x is greater than 5")
    print("x is definitely positive")

# Nested indentation
y = 20
if y > 10:
    print("y is greater than 10")
    if y > 15:
        print("y is also greater than 15")

# Indentation with for loop
print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(i, end=" ")

# Indentation with while loop
print("\n\nCountdown:")
count = 5
while count > 0:
    print(count, end=" ")
    count -= 1
print("Done!")

# Functions and indentation
def greet(name):
    message = "Hello, " + name + "!"
    print(message)
    return message

greet("Alice")
greet("Bob")

print("\n" + "=" * 60)
print("PART 2: RESERVED WORDS")
print("=" * 60)

# Python reserved words cannot be used as variable names
reserved_words = [
    "False", "None", "True", "and", "as", "assert",
    "async", "await", "break", "class", "continue",
    "def", "del", "elif", "else", "except", "finally",
    "for", "from", "global", "if", "import", "in",
    "is", "lambda", "nonlocal", "not", "or", "pass",
    "raise", "return", "try", "while", "with", "yield"
]

print("Python Reserved Words:")
print("-" * 40)

for i, word in enumerate(reserved_words):
    print(f"{word:15}", end="")
    if (i + 1) % 5 == 0:
        print()

print("\n")

# Check if a word is reserved using keyword module
import keyword

test_words = ["for", "while", "my_var", "class", "function", "return"]
print("Testing if words are reserved:")
for word in test_words:
    is_reserved = keyword.iskeyword(word)
    print(f"{word:15} -> {'Reserved' if is_reserved else 'Not Reserved'}")

print("\n" + "=" * 60)
print("PART 3: DATA TYPES AND TYPE CASTING")
print("=" * 60)

# NUMERIC TYPES
print("\nNUMERIC TYPES")

# Integer (int) - whole numbers
x = 10
y = -5
z = 0
print(f"Integer examples: {x}, {y}, {z}")
print(f"Type of {x}: {type(x)}")

# Float - decimal numbers
pi = 3.14159
temperature = -2.5
scientific = 1.5e10
print(f"\nFloat examples: {pi}, {temperature}, {scientific}")
print(f"Type of {pi}: {type(pi)}")

# Complex numbers
complex1 = 3 + 4j
complex2 = complex(2, 3)
print(f"\nComplex examples: {complex1}, {complex2}")
print(f"Real part of {complex1}: {complex1.real}")
print(f"Imaginary part of {complex1}: {complex1.imag}")

# BOOLEAN TYPE
print("\nBOOLEAN TYPE")

is_student = True
is_graduated = False
print(f"Boolean examples: {is_student}, {is_graduated}")
print(f"Type of {is_student}: {type(is_student)}")

print(f"\nTrue + True = {True + True}")
print(f"True * 10 = {True * 10}")
print(f"False + 1 = {False + 1}")

a = True
b = False
print(f"\n{a} and {b} = {a and b}")
print(f"{a} or {b} = {a or b}")
print(f"not {a} = {not a}")

# STRING TYPE
print("\nSTRING TYPE")

name = "Python"
greeting = 'Hello, World!'
multi_line = """This is a
multi-line string"""
empty_string = ""

print(f"String examples:")
print(f"  name: {name}")
print(f"  greeting: {greeting}")
print(f"  multi_line: {multi_line}")
print(f"  empty_string: '{empty_string}'")

print(f"\nString operations:")
print(f"  Length of '{name}': {len(name)}")
print(f"  Uppercase: {name.upper()}")
print(f"  Lowercase: {name.lower()}")
print(f"  Reverse: {name[::-1]}")

print("\nString indexing:")
word = "PYTHON"
print(f"  Word: {word}")
print(f"  First character: {word[0]}")
print(f"  Last character: {word[-1]}")
print(f"  Character at index 2: {word[2]}")

print("\nString slicing:")
print(f"  First 3 characters: {word[:3]}")
print(f"  Last 3 characters: {word[-3:]}")
print(f"  Characters from index 1 to 4: {word[1:5]}")

# TYPE CASTING
print("\nTYPE CASTING")

num_str = "42"
num_int = int(num_str)
num_float = float(num_str)

print(f"String '{num_str}' cast to int: {num_int}")
print(f"String '{num_str}' cast to float: {num_float}")

pi_float = 3.14159
pi_int = int(pi_float)
print(f"\nFloat {pi_float} cast to int: {pi_int}")

age = 25
age_str = str(age)
print(f"\nInt {age} cast to string: '{age_str}'")

print(f"\nTrue as int: {int(True)}")
print(f"False as int: {int(False)}")
