
#import mysql.sql.connector
import pymysql

db= pymysql.connect(
    host ="localhost",
    user = "root",
    password = "mysql123",
    database = "Customers"
)

c=db.cursor()
c.execute("SELECT * FROM policys")
for i in c:
    print(i)
db.close()


