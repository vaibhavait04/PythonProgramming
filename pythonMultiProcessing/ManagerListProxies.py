from multiprocessing import Manager
manager = Manager() 
a = manager.list()
b = manager.list()
a.append(b)         # referent of a now contains referent of b
print(a, b)
b.append('hello')
print(a, b)
