

def get_input():
    key=input("Enter the Key:\n")
    value=input("Enter the Value:\n")
    return key,value

def main():
    K,V=get_input()
    D1={K:V}  # Dictionary
    S1={K,V}  # Set
    print(type(D1))
    key_list=['a','e','i','o','u']
    value_list=[1,2,3,4,5]
    D2={'math':100, 'science':85}
    D3=dict(name='Ram',age=23)
    D4=dict(zip(key_list,value_list))
    D5=dict.fromkeys(['a','b'])
    print(D3,D4,D5)
    D5['a']=3
    print(D5['a'])
    print(D4.keys(),D4.values(),D4.items(),len(D4))
    print(D4.get('k',6))
    D4.update(D2)
    print(D4)
    D4.pop('e')
    print(D4)
main()



















# https://whiteboard.office.com/me/whiteboards/cef1c598-318b-49f6-9b69-4e9af6f8f2f0