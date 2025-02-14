#Write a Python program to do arithmetical operations addition and division.

a = float(input("Enter First number : "))
b = float(input("Enter Second number : "))

# addition 

print(f"{a} + {b} = { a + b }")

# division 

if b == 0:
    print("Invalid division")
else:
    print(f"{a} / {b} = { a / b }")