#Temperature conversion program

print(" 1. Fahrenheit -> Celsius \n 2. Celsius -> Fahrenheit")

option = int(input("Enter the option:"))
if option == 1:
    f = float(input("Enter the temperature in Fahrenheit: "))
    c = (f - 32) * (5/9)
    print(f"Temperature in celsius is {c}")
else:
    c = float(input("Enter the temperature in Celsius: "))
    f = ((9/5) * c) + 32
    print(f"Temperature in fahrenheit is {f}")
