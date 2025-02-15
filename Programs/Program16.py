#Write a program to find the factorial of the number

num = int(input("Enter the number : "))

if num<0:
    print(f"Factorial of {num} does not Exist")
elif num == 0:
    print(f"Factorial of {num} is 1")
else:
    factorial = 1
    for i in range (1,num+1):
        factorial = factorial * i

    print(f"Factorial of {num} is {factorial}")
