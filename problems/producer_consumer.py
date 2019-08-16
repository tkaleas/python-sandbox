from threading import Thread
from threading import Lock
from threading import Condition
import random

# CLASSIC PRODUCER CONSUMER PROBLEM, FIXED SIZED BUFFER
# uses Python threading module with locks/conditions
# https://docs.python.org/3/library/threading.html

lock = Lock()

#Lock with Notify/Wait + Acquire/Release
condition = Condition()

class IntBuffer(object):
    def __init__(self):
        self.index = 0
        self.buffer = [None]*10  #Fixed Sized Buffer

    def add(self,num):
        with condition:
            while self.index >= len(self.buffer):
                print("Queue is Full, Waiting")
                condition.wait()
            self.buffer[self.index] = num
            self.index += 1
            #notify other threads to wake up
            condition.notify_all()

    def remove(self):
        with condition:
            while self.index < 0:
                print("Queue is Empty, Waiting to Remove")
                condition.wait()
            self.buffer[self.index] = None
            self.index -= 1
            return self.buffer[self.index]


class Producer(Thread):
    def __init__(self, inputBuffer):
        self.buffer = inputBuffer
        super(Producer, self).__init__()

    def run(self):
        while True:
            num = random.randint(0,10)
            self.buffer.add(num)
            print("Produced: {}".format(num))


class Consumer(Thread):
    def __init__(self, inputBuffer):
        self.buffer = inputBuffer
        super(Consumer, self).__init__()

    def run(self):
        while True:
            num = self.buffer.remove()
            print("Consumed: {}".format(num))

def start_produce_consumer_cycle():
    buf = IntBuffer()
    prod = Producer(buf)
    con = Consumer(buf)
    prod.start()
    con.start()

start_produce_consumer_cycle()