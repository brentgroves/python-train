# https://flask-restful.readthedocs.io/en/latest/quickstart.html#a-minimal-api
# https://ch-rowley.github.io/2021/10/24/How-to-marshal-data-with-Flask.html
# https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html
# https://curl.se/docs/manpage.html#-k
import email
from flask import Flask, request
from flask_restful import Resource, abort, Api, reqparse
from marshmallow import Schema, fields
from marshmallow import ValidationError
import trial_balance.parameters  as trial_balance_parameters
import mean_time_between_failues.parameters as mean_time_between_failures_parameters
import daily_metrics.parameters as daily_metrics_parameters
import os

app = Flask(__name__)
api = Api(app)

# class Parameters(Schema):
#     report_name = fields.Str(required=True)
#     email = fields.Email(required=True)
#     start_period = fields.Int(required=True)
#     end_period = fields.Int(required=True)

# parameters = Parameters()

class ReportList(Resource):
# Get
    # curl http://localhost:5000/report_list
    def get(self):
        return "trial_balance,daily_metrics,mean_time_between_failures"

# Thank you, Father for the work that you give us.
api.add_resource(ReportList, '/report_list')

class Report(Resource):
# Get
    # curl http://localhost:5000/report/trial_balance
    def get(self,report_name):
        return_value = os.system('ls -l')
        print(f"return_value={return_value}")
        # return_value = os.system('ls -l')
        # print(f"return_value={return_value}")
        return_value = ''
        match report_name:
            case 'trial_balance':
                return_value = """curl -X POST http://localhost:5000/report -H 'Content-Type: application/json' -d '{"report_name":"trial_balance","email":"username@buschegroup.com","start_period":202201,"end_period":202207}' Please remove all the backslashes and replace username@buschegroup.com with your username.""" 
            case 'daily_metrics':
                return_value = """curl -X POST http://localhost:5000/report -H 'Content-Type: application/json' -d '{"report_name":"daily_metrics","email":"username@buschegroup.com","start_period":202201,"end_period":202207}' Please remove all the backslashes and replace username@buschegroup.com with your username."""     
            case 'mean_time_between_failures':
                return_value = """curl -X POST http://localhost:5000/report -H 'Content-Type: application/json' -d '{"report_name":"mean_time_between_failures","email":"username@buschegroup.com","start_period":202201,"end_period":202207}' Please remove all the backslashes and replace username@buschegroup.com with your username."""     
        return return_value
# Post    
    # curl -X POST http://localhost:5000/report -H 'Content-Type: application/json' -d '{"report_name":"trial_balance","email":"username@buschegroup.com","start_period":202201,"end_period":202207}'
    def post(self):
        parameters = request.get_json()
        try:
            report_name=parameters['report_name']
            match report_name:
                case 'trial_balance':
                    parameters_dict = trial_balance_parameters.parameters.load(request.get_json())
                case 'daily_metrics':
                    parameters_dict = daily_metrics_parameters.parameters.load(request.get_json())
                case 'mean_time_between_failures':
                    parameters_dict = mean_time_between_failures_parameters.parameters.load(request.get_json())
            # https://janakiev.com/blog/python-shell-commands/

        except ValidationError as err:
            return err.messages, 422
        return f"report_name:{parameters_dict['report_name']},email:{parameters_dict['email']},start_period:{parameters_dict['start_period']},end_period:{parameters_dict['end_period']}"
        # return 'report in progress... email will be sent shortly.' 

# Thank you, Father for the work that you give us.
api.add_resource(Report, '/report/<string:report_name>','/report')


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
# For posted form input, use request.form.
# email = request.form.get('email')
# https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request
# https://flask.palletsprojects.com/en/2.2.x/api/#flask.Request
    def put(self, hotel_id):
        email = request.form.get('rooms')
        # hotels[hotel_id] = request.form['data']
        # hotels[hotel_id] = request.form['data']
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