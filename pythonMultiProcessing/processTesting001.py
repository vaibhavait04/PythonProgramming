import multiprocessing 
from multiprocessing import Process

def f(name):
    print('hello', name)

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    print ("Process is alive state {0} , total cpu count {1} ".format( p.is_alive() , multiprocessing.cpu_count() ))
    print ("Processes active children {0}".format(multiprocessing.active_children()))
    p.join()
    print("process return {0}".format(p.exitcode))
