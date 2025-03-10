
import threading
import time

def task(lock):
    with lock:
        print(f"{threading.current_thread().name} has accquired the Lock.")
        time.sleep(2)
        print(f"{threading.current_thread().name} has released the Lock")

lock=threading.Lock()