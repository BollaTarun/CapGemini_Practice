

import pymysql

def create_connection():
    db=pymysql.connect(
        host ="localhost",
        user = "root",
        password = "mysql123",
        database = "Customers"
    )
    print("Connection Done Successfully!!!")
    return db

def create_table(db):
    c=db.cursor()
    try:
        query="CREATE TABLE Emp(Name varchar(30),Id INT,dept varchar(20))"
        c.execute(query)
        print("Table Created Successfully!!")
    except pymysql.connect.Error as err:
        print("Something Went Wrong!!")
    finally:
        c.close()

def insert_data(db):
    c=db.cursor()
    try:
        query="INSERT DATA INTO Emp('Raj',20,'CSM')"
        c.execute(query)
        print("Data Inserted Successfully!!")
    except pymysql.connect.Error as err:
        print("Something Went Wrong!!")
    finally:
        c.close()

def update_data(db):
    c=db.cursor()
    try:
        query="UPDATE Emp SET Name='Veera' where ID=20;"
        c.execute(query)
        print("Data Updated Successfully!!")
    except pymysql.connect.Error as err:
        print("Something Went Wrong!!")
    finally:
        c.close()

def drop_data(db):
    c=db.cursor()
    try:
        query="CREATE TABLE Emp(Name varchar(30),Id INT,dept varchar(20))"
        c.execute(query)
        print("Table Created Successfully!!")
    except pymysql.connect.Error as err:
        print("Something Went Wrong!!")
    finally:
        c.close()

def delete_table(db):
    c=db.cursor()
    try:
        query="DROP TABLE Emp;"
        c.execute(query)
        print("Table Deleted Successfully!!")
    except pymysql.connect.Error as err:
        print("Something Went Wrong!!")
    finally:
        c.close()

def display_table(db):
    c=db.cursor()
    try:
        query="SELECT * FROM Emp;"
        c.execute(query)
    except pymysql.connect.Error as err:
        print("Something Went Wrong!!")
    finally:
        c.close()

db=create_connection()
create_table(db)
insert_data(db)
display_table(db)
update_data(db)
display_table(db)
delete_table(db)



# import mysql.connect
# def connect_db():
#     try:
#         connection=mysql.connect.connect(
#             host='localhost',
#             user='root',
#             password='root',
#             database='department'
#         )
#         print('Mysql connected Succesfully')
#         return connection
#     except mysql.connect.Error as err:
#         print(f"Something went wrong: {err}")
# def create_table(connection):
#     cursor=connection.cursor()
#     try:
#         query="""CREATE TABLE EMPLOYEE (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT, salary INT);"""
#         cursor.execute(query)
#         print('Table created Succesfully')
#     except mysql.connect.Error as err:
#         print(f"Something went wrong: {err}")
#     finally:
#         cursor.close()
# def inserting_data(connection):
#     cursor=connection.cursor()
#     try:
#         query="""INSERT INTO EMPLOYEE(name,age,salary) VALUES(%s,%s,%s)"""
#         n=int(input("Enter the no of records to be inserted:"))
#         data=[]
#         for i in range(n):
#             name=input("Enter the name of employee:")
#             age=int(input("Enter the age of employee:"))
#             salary=int(input("Enter the salary of employee:"))
#             data.append((name,age,salary))
#         cursor.executemany(query,data)
#         connection.commit()
#         print('Data Inserted Succesfully')
#     except mysql.connect.Error as err:
#         print(f"Something went wrong: {err}")
#     finally:
#         cursor.close()
# def select_all_data(connection):
#     cursor=connection.cursor()
#     try:
#         query="""SELECT * FROM EMPLOYEE;"""
#         cursor.execute(query)
#         result = cursor.fetchall()
#         for row in result:
#             print(row)
#     except mysql.connect.Error as err:
#         print(f'Something went wrong: {err}')
#     finally:
#         cursor.close()
# def updating_data(connection):
#     cursor=connection.cursor()
#     try:
#         query="""UPDATE EMPLOYEE SET SALARY=7000 WHERE name="shanmuk";"""
#         cursor.execute(query)
#         connection.commit()
#         print('Updated the data succesfully')
#     except mysql.connect.Error as err:
#         print(f"Something went wrong: {err}")
#     finally:
#         cursor.close()
# def deleting_data(connection):
#     cursor=connection.cursor()
#     try:
#         query="""DELETE FROM EMPLOYEE WHERE ID=1;"""
#         cursor.execute(query)
#         connection.commit()
#         print('Data deleted succesfully')
#     except mysql.connect.Error as err:
#         print(f"Something went wrong: {err}")
#     finally:
#         cursor.close()
# def sort_data(connection):
#     cursor = connection.cursor()
#     try:
#         query = """SELECT * FROM EMPLOYEE ORDER BY SALARY DESC;"""
#         cursor.execute(query)
#         result=cursor.fetchall()
#         for row in result:
#             print(row)
#     except mysql.connect.Error as err:
#         print(f'Something went wrong:{err}')
#     finally:
#         cursor.close()
# def query_with_filter(connection):
#     cursor=connection.cursor()
#     try:
#         query="""SELECT * FROM EMPLOYEE WHERE SALARY>%s;"""
#         cursor.execute(query,(5000,))
#         result=cursor.fetchall()
#         for row in result:
#             print(row)
#     except mysql.connect.Error as err:
#         print(f'Something went wrong:{err}')
#     finally:
#         cursor.close()
# def drop_table(connection):
#     cursor=connection.cursor()
#     try:
#         query="""DROP TABLE EMPLOYEE;"""
#         cursor.execute(query)
#         connection.commit()
#         print('Table dropped succesfully')
#     except mysql.connect.Error as err:
#         print(f"Something went wrong: {err}")
#     finally:
#         cursor.close()
# def drop_database(connection):
#     cursor = connection.cursor()
#     try:
#         query = """DROP DATABASE department;"""
#         cursor.execute(query)
#         connection.commit()
#         print('Database dropped succesfully')
#     except mysql.connect.Error as err:
#         print(f"Something went wrong: {err}")
#     finally:
#         cursor.close()
# def main():
#     connection=connect_db()
#     if not connection:
#         return None
#     # create_table(connection)
#     # inserting_data(connection)
#     # updating_data(connection)
#     # deleting_data(connection)
#     # sort_data(connection)
#     # query_with_filter(connection)
#     # drop_table(connection)
#     select_all_data(connection)
#     # drop_database(connection)
#     connection.close()
#     print('Mysql connection closed')
# main()
