from threading import Semaphore, Thread
import time

def producer(sem, shared_data):
    for i in range(5):
        sem.acquire()
        shared_data.append(f"Data {i}")
        print(f"Produced: Data {i}")
        sem.release()
        time.sleep(1)

def consumer(sem, shared_data):
    for i in range(5):
        sem.acquire()
        if shared_data:
            item = shared_data.pop(0)
            print(f"Consumed: {item}")
        sem.release()
        time.sleep(2)

def run_synchronization():
    sem = Semaphore(1)
    shared_data = []
    producer_thread = Thread(target=producer, args=(sem, shared_data))
    consumer_thread = Thread(target=consumer, args=(sem, shared_data))

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()
