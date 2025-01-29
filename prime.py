
# import math

# def data():
#     L=int(input("Enter the Lower Limit:\n"))    
#     N=int(input("Enter the Upper Limit:\n"))
#     return (L,N)

# def check(N):
#     for i in range(L,N+1,1):
#         if(i<2):
#             continue
#             #return False
#         elif i==2:
#             print(i,end=" ")
#             continue
#         elif i%2==0:
#             continue           
#         else:
#             a=0
#             for j in range(3,int(math.sqrt(i))+1,2):
#                 if i%j==0:
#                     a=1
#                     break
#             if a==0:
#                 print(f"{i}",end=" ")
    
# def main():
#     L,N=data()
#     check(L,N)
    
#     #dis.dis(check)
# main()

import math

def data():
    N=int(input("Enter the Number:\n"))
    return N

def check(N):
    if(N<2):
        return False
    elif N==2:
        return True
    elif N%2==0:
        return False          
    else:
        for i in range(3,int(math.sqrt(N)),2):
            if N%i==0:
                return False
        return True
    
def main():
    N=data()
    V=check(N)
    print(f"{V}")
main()