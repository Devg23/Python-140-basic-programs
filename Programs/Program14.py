# Write a program to check if a number is prime or not.
import math

num = int(input("Enter the number : "))

upper = int(math.sqrt(num))
flag = False
if num == 1 or num == 0:
    print(f"{num} is not a prime number")
else:    
    for i in range (2,upper+1):
        if num%i == 0:
            flag = True
            break


if flag == True:
    print("Number is not prime")
else:
    print("Number is prime")    
