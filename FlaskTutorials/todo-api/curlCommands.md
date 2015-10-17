
GET Requests: 
$ curl -i http://localhost:5000/todo/api/v1.0/tasks

POST Requests: 
$ curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://localhost:5000/todo/api/v1.0/tasks

UPDATE Requests: 
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"done":true}' http://localhost:5000/todo/api/v1.0/tasks/2


Authentication: 
$ flask/bin/pip install flask-httpauth
