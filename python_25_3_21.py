import threading
import time

def f():
    print("hello world")
    myThread.run()

if __name__ == '__main__':
    myThread = threading.Timer(3, f)
    myThread.start()
    time.sleep(10)
    if myThread.is_alive():
        myThread.cancel()