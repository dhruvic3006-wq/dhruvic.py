#Arithmetic operator
a = 10
b = 3

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
print(a // b)  # Floor division
print(a % b)   # Modulus
print(a ** b)  # Power
#Assignment operator
x = 10

x += 5
print(x)   # 15

x -= 3
print(x)   # 12

x *= 2
print(x)   # 24

x /= 4
print(x)   # 6.0

x **= 2
print(x)   # 36.0
#unary operator
x = -10
y = -x
print(y)    # 10
#Relational oprerators
x = 10
y = 20

if x < y:
    print("x is less than y")
else:
    print("x is greater than or equal to y")
#logical operators
x = 10
y = 5
z = 15

if (x < y and y < z) or not(z == 15):
    print("Condition is True")
else:
    print("Condition is False")
#Boolean operator
x = 7
y = 5
z = 10

if (x > y and y < z) or not(x == z):
    print("Complex condition is True")
else:
    print("Complex condition is False")
#Bitwise operator
# Bitwise AND
print(5 & 3)    # 1 (binary 101 & 011 = 001)

# Bitwise OR
print(5 | 3)    # 7 (binary 101 | 011 = 111)

# Bitwise XOR
print(5 ^ 3)    # 6 (binary 101 ^ 011 = 110)

# Bitwise NOT
print(~5)       # -6 (binary ~101 = 010 + 1 = -6)

# Left Shift
print(5 << 1)   # 10 (binary 101 << 1 = 1010)

# Right Shift
print(5 >> 1)   # 2 (binary 101 >> 1 = 10)
#Membership operators
'b' not in 'apple'    # True
3 not in [1, 2, 3]    # False

