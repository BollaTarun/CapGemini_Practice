
# Input of 4 Numbers :
def info():
    a=float(input("Enter the 1st Number :\n"))
    b=float(input("Enter the 2nd Number :\n"))
    c=float(input("Enter the 3rd Number :\n"))
    d=float(input("Enter the 4th Number :\n"))
    return (a,b,c,d)

# Calculates the Sum of 4 numbers
def cal_sum(a,b,c,d):
    S=(a+b+c+d)
    return S

# Calculates the Average of 4 numbers
def cal_avg(S):
    A=S/4
    return A

# Display the output
def display(avg):
    print(f"Average of 4 Numbers : {avg}")

# Main Function
def main():
    a,b,c,d= info()
    s=cal_sum(a,b,c,d)
    avg=cal_avg(s)
    display(avg)
main()