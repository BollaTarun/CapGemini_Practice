import math

def data():
    while True:
        L=int(input("Enter the Lower Limit:\n"))    
        N=int(input("Enter the Upper Limit:\n"))
        if(L>0 and L<N):
            return (L,N)
        else:
            print("Enter valid range.")

def check(L,N):
    while L<N+1:
        if(L<2):
            L+=1
            continue
        elif L==2:
            print(L,"is the least prime number.")
            L+=1
            continue
        elif L%2==0:
            L+=1
            continue           
        else:
            a=0
            i=3
            while i<(int(math.sqrt(L))+1) :
                if L%i==0:
                    a=1
                    break
                i+=2
            if a==0:
                print(f"{L}",end="  ")
            L+=1

def main():
    L,N=data()
    check(L,N)
    
    #dis.dis(check)
main()
