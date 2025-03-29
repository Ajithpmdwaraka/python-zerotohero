# Using multithreading to run tasks concurrently

import threading
import time

def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)

thread1 = threading.Thread(target=print_numbers)
thread1.start()

print("Main thread continues execution...")
