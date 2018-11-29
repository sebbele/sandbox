import time, threading

def set_interval(callback, seconds):
    memoize = {"stop": False, "latestRun": time.time()}

    def looper():
        start = time.time()
        callback(start - memoize["latestRun"], stopper)
        delta = time.time() - start

        if memoize["stop"] == False:
            memoize["latestRun"] = time.time()
            threading.Timer(seconds - delta, looper).start()

    def stopper():
        memoize["stop"] = True

    looper()

    return stopper

def foo(dt, stopper):
    print(dt, time.ctime())

stop = set_interval(foo, 0.25)
threading.Timer(5, stop).start()
