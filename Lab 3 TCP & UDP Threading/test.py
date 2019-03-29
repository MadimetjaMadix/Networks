
#!/usr/bin/python


import threading
import time
from threading import Thread

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.delay = delay
    def run(self):
        print("\nStarting " + self.name)
        print(self)
        print_time(self.name, self.counter, self.delay)
        print("\nExiting " + self.name)

def print_time(threadName, counter, delay):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("\n%s: %s %d" % (threadName, time.ctime(time.time()),counter))
        print(threading.active_count())
        counter -= 1

# Create new threads
#thread1 = myThread(1, "Thread-1", 2, 1)
#thread2 = myThread(2, "Thread-2", 5, 2)
thread3 = Thread(target=print_time, args=("Thread-3", 3, 1))
thread4 = Thread(target=print_time, args=("Thread-4", 4, 3))

# Start new Threads
#thread1.start()
#thread2.start()
thread3.run()
thread4.run()

# Join threads
#thread1.join()
#thread2.join()
thread3.join()
thread4.join()

print("Exiting Main Thread")
