import math
# Default Math Values :
print("Pi : ",math.pi)
print("Euler's Number :",math.e)

# Some Basic Math Functions :
 # Math.sqrt()
N=121
R=math.sqrt(N)
print(f"Square of {N} : {R}")

# Math.pow()
b=20
e=2
R=math.pow(b,e)
print(f"Value : {R}")

#   abs()
K=-34
print(f"Abs of {K} :{abs(K)}")

#  Trigonometric Functions

A=math.radians(45)
print(f"Sin of {A} : {math.sin(A)}")
print(f"Cos of {A} : {math.cos(A)}")
print(f"Tan of {A} : {math.tan(A)}")

#  Logarithmic Functions
K=10
print(f"Log of {K} : {math.log(K)}")
print(f"Natural Log of {K} : {math.log10(K)}")

# Rounding Functions
print(math.ceil(9.002))
print(math.floor(9.9999))
