import threading

def function(i):
    print("function called from thread {0}, {1} \n".format(i,threading.currentThread().getName()))
    return

thread = [] 

for i in range(5):
    t = threading.Thread(target=function, args = (i,))
    threads.append(t)
    t.start()

for i in range(5):
    threads[i].join()

