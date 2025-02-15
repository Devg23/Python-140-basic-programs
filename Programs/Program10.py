#Write a python program to swap two variable without using temp

a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))

a,b = b,a

print(f"After swapping value of a is {a} and value of b is {b}")