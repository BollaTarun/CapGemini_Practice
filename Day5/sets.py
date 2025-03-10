

def main():
    S={1,2,3,4}
    T={3,6,2,9}
    print(S.union(T))   # S|T
    print(S.intersection(T)) # S&T
    print(S-T)  # S.difference(T)
    print(T-S)  # T.difference(S)
main()