from multiprocessing import Pool
from time import sleep

from contextlib import contextmanager
@contextmanager
def terminating(thing):
    try:
        yield thing
    finally:
        thing.terminate()

def f(x):
    return x*x

if __name__ == '__main__':
    # start 4 worker processes
    with terminating(Pool(processes=10)) as pool:

        # print "[0, 1, 4,..., 81]"
        print(pool.map(f, range(10)))

        # print same numbers in arbitrary order
        l = [ i for i in pool.imap_unordered(f, range(10)) ]
        print("{0}".format(l) )

        # evaluate "f(10)" asynchronously
        res = pool.apply_async(f, [10])
        print(res.get(timeout=2))             # prints "100"

        # make worker sleep for 10 secs
        res = pool.apply_async(sleep, [10])
        print(res.get(timeout=2))             # raises multiprocessing.TimeoutError

    # exiting the 'with'-block has stopped the pool


