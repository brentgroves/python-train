https://flask-restful.readthedocs.io/en/latest/quickstart.html#a-minimal-api

https://flask-restful.readthedocs.io/en/latest/
https://flask-restful.readthedocs.io/en/latest/quickstart.html#a-minimal-api

$ curl http://localhost:5000/todo1 -d "data=Remember the milk" -X PUT
{"todo1": "Remember the milk"}
$ curl http://localhost:5000/todo1
{"todo1": "Remember the milk"}
$ curl http://localhost:5000/todo2 -d "data=Change my brakepads" -X PUT
{"todo2": "Change my brakepads"}
$ curl http://localhost:5000/todo2
{"todo2": "Change my brakepads"}