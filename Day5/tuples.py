

# def get_input():
#     T=()
#     N=int(input("Enter the Size of Input:\n"))
#     for i in range(N):
#         T.add(input(f"Enter Element {i+1} :\n"))
#     return T

def main():
    #T=get_input()
    #print(T)
    T1=()
    T2=(0,'av',"@",3434)
    T3=("abc",(0,'eagle'))
    T4=tuple("eggs")
    print(len(T4))
    print(T4[0:5])
    print(T1,T2,T3,T4)

    # Tuples : Ordered, Immutable (unchangable) ,store multiple data types , allow duplicates
    # Allows negative  indexes : T[-2]
    # Check if element exists :
#         thistuple = ("apple", "banana", "cherry")
        # if "apple" in thistuple:
        #   print("Yes, 'apple' is in the fruits tuple")
    # To perform operations, convert it into list using list(), perform operations and 
    #  change it again into tuple using tuple()
    # Add tuples : T1+=T2
    # del T : Deletes entire tuple
    # 
main()
