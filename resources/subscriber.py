from flask_restful import reqparse, Resource
from models.subscriber import SubscriberModel

class Subscriber(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('')