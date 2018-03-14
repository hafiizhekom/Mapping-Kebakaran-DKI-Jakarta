from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import json
from flask.ext.jsonpify import jsonify

#db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)

class Hydrant(Resource):
    def get(self):
        with open('Hydrant/hydrant.json') as json_data:
            d = json.load(json_data)
        return jsonify(d)

class Possektor(Resource):
    def get(self):
        with open('Pos Sektor Kebakaran/possektor.json') as json_data:
            d = json.load(json_data)
        return jsonify(d)

class Kebakaran(Resource):
    def get(self):
        with open('Kebakaran/kebakaran.json') as json_data:
            d = json.load(json_data)
        return jsonify(d)
    
#class Employees_Name(Resource):
#    def get(self, employee_id):
#        conn = db_connect.connect()
#        query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
#        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
#        return jsonify(result)
        

api.add_resource(Hydrant, '/hydrant') # Route_1
api.add_resource(Possektor, '/possektor') # Route_1
api.add_resource(Kebakaran, '/kebakaran') # Route_2
#api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3


if __name__ == '__main__':
    app.run(debug=True)
     
