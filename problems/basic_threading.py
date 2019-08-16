from threading import Thread
import urllib.request
import time

#Basic Threading Example
from threading import Lock

class GetUrlThread(Thread):
    def __init__(self, url):
        self.url = url
        super(GetUrlThread, self).__init__()

    def run(self):
        resp = urllib.request.urlopen(self.url)
        print(self.url, resp.getcode())

def get_responses():
    urls = ['https://www.google.com', 'https://www.ebay.com', 'https://www.alibaba.com', 'http://www.reddit.com']
    start = time.time()
    threads = []
    for url in urls:
        t = GetUrlThread(url)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("Elapsed time: %s" % (time.time()-start))

#get_responses()


## RACE CONDITION FIX WITH Lock()
#define a global variable
some_var = 0
lock = Lock()

class IncrementThread(Thread):
    def run(self):
        #we want to read a global variable
        #and then increment it
        global some_var
        lock.acquire()
        read_value = some_var
        print("some_var in {} is {}".format(self.name, read_value))
        some_var = read_value + 1
        print("some_var in {} after increment is {}".format(self.name, some_var))
        lock.release()

def use_increment():
    threads = []
    for i in range(50):
        t = IncrementThread()
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("After 50 modifications, some_var should have become 50")
    print("After 50 modifications, some_var is {}".format(some_var))

#use_increment()

## Create Global List Thread
import time

class CreateListThread(Thread):
    def run(self):
        self.entries = []
        for i in range(10):
            time.sleep(1)
            self.entries.append(i)
        lock.acquire()
        print(self.entries)
        lock.release()

def use_create_list_thread():
    for i in range(3):
        t = CreateListThread()
        t.start()

use_create_list_thread()