import queue
import threading
import time

def producer():
    for i in range(5):
        time.sleep(5)
        q.put(i)
        print("Produced :",i)

def consumer():
    while True:
        item=q.get()
        if item is None:
            break
        print("Consumed :",item)
        time.sleep(2)


q=queue.Queue()
produce_thread=threading.Thread(target=producer)
consume_thread=threading.Thread(target=consumer)
produce_thread.start()
consume_thread.start()

produce_thread.join()
q.put(None)

consume_thread.join()
print("Thread Communication Completed!!")


