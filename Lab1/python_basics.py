# Lab 1: Python Basics
# This file covers Python syntax, input/output, and multiple statements

print("=" * 60)
print("PART 1: PYTHON SYNTAX")
print("=" * 60)

# Simple print statement
print("Hello, World!")

# Print with multiple arguments
print("Python", "is", "a", "general-purpose", "language")

# Print with different data types
print("Integer:", 42)
print("Float:", 3.14)
print("String:", "Hello")

# Print with sep parameter to change separator
print("Python", "is", "fun", sep="-")

# Print with end parameter to change ending
print("Hello", end=" ")
print("World")

print("\n" + "=" * 60)
print("PART 2: INPUT AND OUTPUT")
print("=" * 60)

# Basic input reads a string from user
name = input("Enter your name: ")
print("Hello, " + name + "!")

# Input and storing as different types
age = input("Enter your age: ")
print("Your age is:", age)
print("Type of age:", type(age))

# Converting input to integer
age_int = int(input("Enter your age (as number): "))
print("Next year you will be:", age_int + 1)

# Multiple inputs in one line
print("\nEnter two numbers:")
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")

print("\n" + "=" * 60)
print("PART 3: MULTIPLE STATEMENTS ON A SINGLE LINE")
print("=" * 60)

# Multiple assignment statements
a = 10; b = 20; c = 30
print("a =", a, ", b =", b, ", c =", c)

# Multiple print statements
print("Hello"); print("World"); print("!")

# Multiple operations
x = 5; y = 10; print("Sum:", x + y)

# Demonstrating semicolon usage
name = "Python"; version = 3; print(name, "version", version)
