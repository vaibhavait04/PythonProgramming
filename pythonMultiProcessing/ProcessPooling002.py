from multiprocessing import Pool
import os


def work(files):
    var = [os.getpid(), os.getpid()+1]
    print ("Files {0} by PID {1}".format(files,os.getpid()))
    return var

pool = Pool(processes=4)

#result = pool.map_async(work, ("%d.txt"%n for n in xrange(1,21)))
x = ("%d.txt"%n for n in xrange(1,21))
print "value of x is {0}".format(x) 
result = pool.map_async(work, x)

result = result.get()
result.sort()
print (result)

