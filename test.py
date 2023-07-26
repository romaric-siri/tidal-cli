import logging

import threading

import time


def thread_function(name):

    logging.info("Thread %s: starting", name)
    a= input("please int")
    print(a)
    logging.info("Thread %s: finishing", name)

def f():
    while True:
        print("started")
        time.sleep(1)



if __name__ == "__main__":


    x = threading.Thread(target=thread_function, args=(1,))
    x.start()

    p = threading.Thread(target=f)
    p.start()
