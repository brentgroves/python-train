# https://flask-restful.readthedocs.io/en/latest/quickstart.html#a-minimal-api
# https://ch-rowley.github.io/2021/10/24/How-to-marshal-data-with-Flask.html
# https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html
from flask import Flask, request
from flask_restful import Resource, abort, Api, reqparse
from marshmallow import Schema, fields
from marshmallow import ValidationError

app = Flask(__name__)
api = Api(app)

hotels = {}
hotel_dict = {}

class HotelSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    state = fields.Str(required=True)
    rooms = fields.Int(required=True)
    start_date = fields.DateTime()


hotel_schema = HotelSchema()

def abort_if_todo_doesnt_exist(hotel_id):
    if hotel_id not in hotels:
        abort(404, message="Hotel {} doesn't exist".format(hotel_id))

class HotelList(Resource):
    # curl http://localhost:5000/hotels
    def get(self):
        return hotels

# curl -X POST http://localhost:5000/hotel -H 'Content-Type: application/json' -d '{"id":"1","name":"name1","state":"state1","rooms":"1"}'
    def post(self):
        v1 = request.get_json()
        try:
            hotel_dict = hotel_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 422

        id = hotel_dict["id"]
        hotels[id] = hotel_dict
        # new_hotel_object = Hotel(**hotel_dict)
        # return {"hotel_id": new_hotel_object.id}, 201        
        return {id: hotels[id]} 


class HotelsAPI(Resource):

# Get
    # curl http://localhost:5000/hotels/1
    def get(self, hotel_id):
        abort_if_todo_doesnt_exist(hotel_id)
        hotel = hotels[hotel_id]
        # hotel = Hotel.query.get(hotel_id)
        # return hotel_schema.dump(hotel)
        return {hotel_id: hotels[hotel_id]}
# Update
# curl http://localhost:5000/hotels/1 -d "rooms=3" -X PUT -v
    def put(self, hotel_id):
        hotels[hotel_id] = request.form['data']
        return {hotel_id: hotels[hotel_id]}
# Delete
# curl http://localhost:5000/hotel/1 -X DELETE -v
    def delete(self, hotel_id):
        abort_if_todo_doesnt_exist(hotel_id)
        del hotels[hotel_id]
        return '', 204

        # Thank you Abba for this work! Can not ouput the datetime field
api.add_resource(HotelList, '/hotel')
api.add_resource(HotelsAPI, '/hotel/<int:hotel_id>')
# api.add_resource(HotelsAPI, '/hotel','/hotel/<string:hotel_id>')

print('curl http://localhost:5000/hotel/1 -d "data=Hotel 1" -X PUT')

# curl -X POST http://localhost:5000/hotel -H 'Content-Type: application/json' -d '{"id":"1","name":"name1","state":"state1","rooms":"2"}'
# curl -X POST http://localhost:5000/hotel
#    -H 'Content-Type: application/json'
#    -d '{"id":"1"}'

todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(TodoSimple, '/<string:todo_id>')

class Todo1(Resource):
    def get(self, todo_id):
        print(todo_id)
        # Default to 200 OK
        return {'task': 'Hello world'}

api.add_resource(Todo1, '/todo1/<string:todo_id>')

class Todo2(Resource):
    def get(self, todo_id):
        print(todo_id)
        # Set the response code to 201
        return {'task': 'Hello world'}, 201

api.add_resource(Todo2, '/todo2/<string:todo_id>')

class Todo3(Resource):
    def get(self,todo_id):
        print(todo_id)
        # Set the response code to 201 and return custom headers
        return {'task': 'Hello world'}, 201, {'Etag': 'some-opaque-string'}

api.add_resource(Todo3, '/todo3/<string:todo_id>')

class Todo4(Resource):
    def get(self,todo_id):
        print(todo_id)
        # Set the response code to 201 and return custom headers
        return {'task': 'Hello world'}, 201, {'Etag': 'some-opaque-string'}

    def put(self,todo_id):
        print(todo_id)
        parser = reqparse.RequestParser()
        parser.add_argument('rate', type=int, help='Rate to charge for this resource')
        args = parser.parse_args()        
        # Set the response code to 201 and return custom headers
        return {'task': 'Hello world'}, 201, {'Etag': 'some-opaque-string'}

api.add_resource(Todo4, '/todo4/<string:todo_id>')

print('from requests import put, get')
print("get('http://localhost:5000/todo2/todo2').json()")

print('curl http://localhost:5000/todo0 -d "data=Remember the milk" -X PUT')
print('curl http://localhost:5000/todo0')
print('curl http://127.0.0.1:5000/todo1/id1')
print('http://127.0.0.1:5000/todo2/id1')
print('http://127.0.0.1:5000/todo3/id1')

if __name__ == '__main__':
    app.run(debug=True)