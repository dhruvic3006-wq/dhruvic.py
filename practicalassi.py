# Simple Interest Calculator

# Input values
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))

# Calculate simple interest
simple_interest = (principal * rate * time) / 100

# Display result
print("Simple Interest is:", simple_interest)
# Find maximum of two numbers

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    print("Maximum number is:", a)
else:
    print("Maximum number is:", b)
# Print numbers from 1 to 5

for i in range(1, 6):
    print(i)
# Find length of a string

text = input("Enter a string: ")
length = len(text)

print("Length of the string is:", length)
# Print a welcome message

print("Welcome to Python Programming!")
# Print first character of a string

text = input("Enter a string: ")

if len(text) > 0:
    print("First character is:", text[0])
else:
    print("String is empty")
# Print last character of a string

text = input("Enter a string: ")

if len(text) > 0:
    print("Last character is:", text[-1])
else:
    print("String is empty")
# Check positive or negative number

num = float(input("Enter a number: "))

if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")
# Add three numbers

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

sum = a + b + c

print("Sum of three numbers is:", sum)
# Take input from user

name = input("Enter your name: ")
print("Hello,", name)


