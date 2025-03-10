
# import threading
# import time

# def single_task():
#     print("Task Started!!")
#     time.sleep(2)
#     print("Task Completed!!")

# thread=threading.Thread(target=single_task)
# thread.start()
# thread.join()
# print("Main Thread Execution Completed!!")

import threading
import time

def even():
    time.sleep(1)
    for i in range(2,11,2):
        print(i,end=" ")
    print()
    time.sleep(1)

def odd():
    time.sleep(1)
    for i in range(1,11,2):
        print(i,end=" ")
    print()
    time.sleep(1)


t1=threading.Thread(target=odd)
t2=threading.Thread(target=even)
#t3=threading.Thread(target=finish_game)
t1.start()
t2.start()
#t3.start()
#t1.join()
t2.join()
#t3.join()
print("DONE!!!")