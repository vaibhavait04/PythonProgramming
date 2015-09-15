from multiprocessing import Process, Lock

def f(l, i):
    l.acquire()
    print ("Lock taken") 
    try:
        print('hello world', i)
    finally:
        l.release()
        print ("Lock released") 

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()


