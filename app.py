from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse

app = Flask(__name__)
api = Api(app)

class Device(Resource):
    def get(self):
        return {'devices':['device 1','device 2','device 3']}, 200


    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name',type=str, help="The name of device is required", trim=True, required=True)
        parser.add_argument('sno', type=str, help="The device must have a device id", trim=True,required=True)
        parser.add_argument('license_keyid',type=int, help="license key has to be mapped", required=False)

        args = parser.parse_args()
        return args, 200

class Subscriber(Resource):
    def get(self):
        return {'subscribers':['subs 1','subs 2', 'subs 3']}


api.add_resource(Subscriber, '/subscriber')
api.add_resource(Device, '/device')


if __name__ == '__main__':
    app.run(debug=True)