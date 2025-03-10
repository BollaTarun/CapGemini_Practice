
import threading
import time

def process_data(data):
    result=sum(data)
    print("Result of Sum :",result)

d1=list(range(100000))
d2=list(range(100000,200000))
d3=list(range(200000,300000))
d=[d1,d2,d3]
for i in range(3):
    thread=threading.Thread(target=process_data(d[i]))
    thread.start()
    thread.join()
    time.sleep(10)