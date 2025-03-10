
# class Product:
#     def __init__(self,product_name,product_id,category_id,brand_id,model_year,list_price):
#         self.product_name=product_name


# class Category:
#     def __init__(self,category_name,category_id):
#         self.category_name=category_name
#         self.category_id=category_id

# class Stocks:
#     def __init__(self,store_id,product_id,quantity):
#         self.store_id=store_id

# class Brand:
#     def __init__(self,brand_id,brand_name):
#         self.brand_id=brand_id
 

class Customers:
    def __init__(self,customer_id,first_name,last_name,phone,email,street,city,state,zipcode):
        self.customer_id=customer_id
        self.first_name=first_name
        self.last_name=last_name
        self.phone=phone
        self.email=email
        self.street=street
        self.city=city
        self.state=state
        self.zipcode=zipcode

    def get_customer_info(self):
        cust=[]
        cust.append(self.customer_id)
        cust.append(self.first_name)
        cust.append(self.last_name)
        cust.append(self.phone)
        return cust
    
class Orders:
    def __init__(self,order_id,order_status,order_date,required_date,shipped_date,store_id,staff_id,customer_id):
        self.customer_id=customer_id
        self.order_id=order_id
        self.order_status=order_status
        self.order_date=order_date
        self.required_date=required_date
        self.shipped_date=shipped_date
        self.store_id=store_id
        self.staff_id=staff_id

    def get_order_info(self):
        ord=[]
        ord.append(self.order_id)
        ord.append(self.order_status)
        ord.append(self.order_date)
        ord.append(self.required_date)
        ord.append(self.shipped_date)
        return ord
    
C=Customers(5,"Raj","Vikram","9393029484","mnp@gm.com","ZP Street","Hyd","Telangana",402921)
print(C.get_customer_info())

O=Orders(9,"Shipped","22-10-2022","29-10-22","25-10-22",32,44,"Telangana",5)
print(C.get_customer_info())


