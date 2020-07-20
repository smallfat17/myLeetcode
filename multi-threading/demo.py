import threading
import time

from threading import Lock




def test(lock, msg):

    for i in range(50):
        lock.acquire()
        print(msg)
        lock.release()
        # time.sleep(.000001)

if __name__ == '__main__':
    lock = Lock()
    thread = threading.Thread(target=test, args=(lock, 'thread1'))
    thread2 = threading.Thread(target=test, args=(lock, 'thread2'))
    print('1start')
    thread.start()
    print('2start')
    thread2.start()
