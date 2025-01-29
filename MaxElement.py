
# Max of 3 Elements :
# # Get the Input Data
# def data():
#     a=float(input("Enter the 1st Number :\n"))
#     b=float(input("Enter the 2nd Number :\n"))
#     c=float(input("Enter the 3rd Number :\n"))
#     return (a,b,c)

# # Identify Maximum Number :
# def max_num(a,b,c):
#     if(a>=b and a>=c):
#         return a
#     elif(b>=c and b>=a):
#         return b
#     else:
#         return c
    
# # Display the output :
# def display(a,b,c,M):
#     print(f"Max Number of {a},{b},{c} : {M}") 

# #Main Function :
# def main():
#     a,b,c=data()
#     M=max_num(a,b,c)
#     display(a,b,c,M)

# main()

# Max of 4 Elements
import dis

def max_num():
    first_maxvar=""
    second_maxvar=""
    a=float(input("Enter 1st Number:\n"))
    b=float(input("Enter 2nd Number:\n"))
    if(a>=b):
        Max1=a
        first_maxvar="a"
    else:
        Max1=b
        first_maxvar_="b"
    c=float(input("Enter 3rd Number:\n"))
    d=float(input("Enter 4th Number:\n"))
    if(c>=d):
        Max2=c
        second_maxvar="c"
    else:
        Max2=d
        second_maxvar="d"
    if(Max1>=Max2):
        return(Max1,first_maxvar)
    else:
        return(Max2,second_maxvar)

def display(max,var):
    print(f"Max No of a,b,c,d is {var} with value {max}")

def main():
    max,var=max_num()
    display(max,var)
    dis.dis(max_num)
    
main()


