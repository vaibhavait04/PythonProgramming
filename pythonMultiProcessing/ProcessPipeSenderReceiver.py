from multiprocessing import Process, Pipe
import os
import time
def f(conn):
    print ("process id : " + str (os.getpid()))
    x= 0 
    while x < 100:
        conn.send(str(x))
        x = x + 1 
        time.sleep (1) 
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p1 = Process(target=f, args=(child_conn,))
    p2 = Process(target=f, args=(child_conn,))
    p1.start()
    p2.start()
    x = parent_conn.recv()
    while x: 
        x = parent_conn.recv()
        print("read value {0}".format(x) )   # prints "[42, None, 'hello']"
    p1.join()
    p2.join()
