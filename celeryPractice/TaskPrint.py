from celery import Celery

app = Celery ('tasks', backend='amqp', broker='amqp://')

#@app.task -> uses more resources without ignore result as true 

@app.task(ignore_result=True)
def print_hello():
	print "hello there" 

