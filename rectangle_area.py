# Area of Rectangle
def display(area):
    print(f"Area of Rectangle : {area}")

def dimensions():
    len=float(input("Enter the Length of the Rectangle :\n"))
    br=float(input("Enter the Breadth of the Rectangle :\n"))
    return (len,br)

def calculate(len,br):
    area=len * br
    return area

def main():
    L,W=dimensions()
    A=calculate(L,W)
    display(A)

main()
