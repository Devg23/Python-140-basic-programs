#Write a program to print the prime numbers in the interval

import math

upper = int(input("Enter the upper bound:"))
print("Prime numbers in the given range are as follows")
for i in range (2,upper+1):
    sq = int(math.sqrt(i))
    flag = False
    for j in range (2,sq+1):
        if i%j == 0:
            flag = True
            break

    if flag == False:
        print(i)    