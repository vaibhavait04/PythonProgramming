from multiprocessing.managers import BaseManager
import queue
queue = queue.Queue()
class QueueManager(BaseManager): pass
QueueManager.register('get_queue', callable=lambda:queue)
m = QueueManager(address=('localhost', 50000), authkey=b'abracadabra')
s = m.get_server()
s.serve_forever()
