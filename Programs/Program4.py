#Write a python program to swap two variables

a = int(input("Enter the value of A : "))
b = int(input("Enter the value of B : "))

temp = a
a = b  #In this part swapping is done
b = temp

print("After swapping")

print(f"Value of A is {a}")
print(f"Value of B is {b}")