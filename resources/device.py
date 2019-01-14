from flask_restful import reqparse, Resource
from models.device import DeviceModel

class Device(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('device_id',type=str, help='Every device must have unique device id', required=True, trim=True)
        parser.add_argument('name', type=str, help='Device name is missing', trim=True, required=True)
        args = parser.parse_args()
        if DeviceModel.find_by_device_id(args['device_id']):
            return {"message":"Device name must be unique"}, 400

        device = DeviceModel(args['name'], args['device_id'])
        device.save_to_db()
        return device.json(), 200