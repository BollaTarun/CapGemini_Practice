#Input of 5 Numbers into a List
def info():
    list=[]
    for i in range(5):
        list.append(int(input(f"Enter the Element {i+1}:\n")))
    return list

# Calculate the sum of array elements
def sum(list):
    sum=0
    for i in range(len(list)):
        sum+=list[i]
    return sum


def display(S):
    print("Sum of Elements : ",S)

def main():
    array=info()
    S=sum(array)
    display(S)
    
main()
