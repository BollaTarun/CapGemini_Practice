# first_name = input("What's your name?\n")
# last_name = input("What's your surname?\n")

# print("Hello !")
# print(f"Hello, {first_name} {last_name}")
# address=input("Please tell your address\n")

# print( f"Hello, Mr.{first_name} {last_name} from {address}")
# Ctrl+K, Ctrl+C : To comment
# Ctrl+K, Ctrl+U : TO uncomment

A = float( input("Enter 1st Number :\n"))
B = float( input("Enter 2nd Number :\n"))
S = A + B
print(S)

N=255
K = int( N / 10 * 10 )  # Restriction of float datatype by type conversion
L = N // 10 * 10        # Integer division 
M= N / 10 * 10          # When division is performed, auto type conversion leads to float
print(K,L,M)

import random
num = random.randint(1,6)
print(num)

# Find roots of a Quadratic Equation :
import math
a=int(input("Enter the co-efficient of x2:\n"))
b=int(input("Enter the co-efficient of x:\n"))
c=int(input("Enter the value of constant :\n"))

R1=(-b+math.sqrt(math.pow(b,2)-4*a*c)) / (2*a) 
R2=(-b-math.sqrt(math.pow(b,2)-4*a*c)) / (2*a) 
print(R1,R2)
