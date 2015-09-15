from multiprocessing import Process, Queue
import os 

def f(q):
    q.put([42, None, 'hello'])
    print('process id:', os.getpid())

if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=f, args=(q,))
    p2 = Process(target=f, args=(q,))
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('process id:', os.getpid())
    print(q.qsize())    # prints "[42, None, 'hello']"
    for x in range(q.qsize()):
        print(q.get())    # prints "[42, None, 'hello']"
