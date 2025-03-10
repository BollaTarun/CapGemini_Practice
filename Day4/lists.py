
def info():
    N=int(input("Enter the Length of List :\n"))
    list=[]
    for i in range(N):
        list.append(int(input(f"Enter the Element {i+1}:\n")))
    return list

def display(list):
    for i in range(len(list)):
        print(list[i],end=" ")

def main():
    array=info()
    display(array)
    L1=[]
    L2=[4,5,[3,6]]
    L3=list("python")
    L4=list(range(-5,8))
    L5=[1,2,3,4,5,6]
    print("Empty List : ",L1) 
    print("2D List : ",L2)
    print("Accessing Elements in a 2D List :",L2[2][0])
    print("Using List : ",L3)
    print("Using Range : ",L4)
    print("Normal List :",L5)
    print(L5[1:20],"\n",L5[-2:4],"\n",L5[-7:],"\n",L5[-5:-2])

    # List ; Mutable , Unordered , store multiple data types, allow duplicates
    # L.insert(elem,pos)        : Insert element at specific position in the list
    # L.append(elem)            : Add element at the end of list
    # L.extend(data structure)  : Add elements of the data structure like list,sets,tuple or dict into the list(L).
    # L.remove(elem)            : Removes the specified element from the list.
    # L.pop(index)              : Removes the element of specified index in list, else the last index.
    # del L[i]                  : Deletes the specified element from the list.
    # del L                     : Deletes the entire list with variable.
    # L.clear()                 : Deletes only the data(content) but not the structure.
    # List Comprehension :
    #   thislist = ["apple", "banana", "cherry"]
    #   [print(x) for x in thislist]
    #  L.sort() : Ascending ,  L.sort(reverse=True) : Descending, L.sort(key=func_name) : Custom Sort
    #  L.reverse()
    #  L1=L2.copy()
    #  L=L1+L2 : To append Lists
    #  L.count(elem) : Returns the count of specified element in list
    #  L.index(elem) : Returns the index of 1st occurence of the element.
main()

