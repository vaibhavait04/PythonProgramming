from multiprocessing import Process, Queue
import os 

def f(q):
    q.put([42, None, 'hello'])
    print('process id:', os.getpid())

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print('process id:', os.getpid())
    print(q.get())    # prints "[42, None, 'hello']"
    p.join()


