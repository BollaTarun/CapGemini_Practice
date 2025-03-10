
# class Employee:
# 	def __init__(self,name,id,age,salary,dept):
# 		self.name=name
# 		self.id=id
# 		self.age=age
# 		self.dept=dept
# 		self.salary=salary

# 	def display(self):
# 		print("Name :",self.name)
# 		print("Age :",self.age)
# 		print("Department :",self.dept)
# 		print("Salary :",self.salary)
# 		print("hello!")
		
        
# # emp1=Employee("Kiran","1","22","200000.00","CSM")
# emp1.display()



class Employee:
	def __init__(self,name,id,age,salary,dept):
		self.name=name
		self.id=id
		self.age=age
		self.dept=dept
		self.salary=salary
		
	def set_salary(self,salary):
		self.salary=salary
		
	def get_salary(self):
		return self.salary

	def set_travel_allowance(self,travel):
		self.salary+=travel
	
	def set_food_allowance(self,food):
		self.salary+=food
	
	def net_salary(self):
		print("Gross Salary : ",self.salary)
		print("Net Salary : ", end=" ")
		print(self.salary-((18)*self.salary)/100)


emp1=Employee("Kiran","1","22",180000.00,"CSM")

emp1.set_travel_allowance(float(input("Enter the Travel Allowance :\n")))
emp1.set_food_allowance(float(input("Enter the Food Allowance :\n")))

emp1.net_salary()



