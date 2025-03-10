
import threading
import time
def daemon_task():
    while True:
        print("Daemon Thread Running......")
        time.sleep(2)

daemon_thread=threading.Thread(target=daemon_task,daemon=True)
daemon_thread.start()

time.sleep(5)
print("Main Thread Running.....")
