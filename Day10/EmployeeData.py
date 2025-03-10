
class Employee:

    emp=[]
    def __init__(self,name,id,dept,age,salary):
        self.name=name
        self.id=id
        self.dept=dept
        self.age=age
        self.salary=salary

    def create_list(self):
        self.emp.append(self.name)
        self.emp.append(self.id)
        self.emp.append(self.dept)
        self.emp.append(self.age)
        self.emp.append(self.salary)
        print(self.emp)

    def write_data(self):
        f=open("C:/Users/iamta/OneDrive/Desktop/Book1.csv","a")
        data=",".join(map(str,self.emp))+"\n"
        print(data+"\n")
        f.write(data)
        f.close()

E=Employee("Raj",33,"IT",30,45000.00)
E.create_list()
E.write_data()

for i in range(2):
    E=Employee(input("Enter the Name:\n"),int(input("Enter the Emp ID:\n")),input("Enter the Emp Department:\n"),int(input("Enter the Employee Age:\n")),int(input("Enter the Employee Salary:\n")))
    E.create_list()
    E.write_data()
    