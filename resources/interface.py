from flask_restful import Resource, request

class Interface(Resource):
  def get(self):
    return ""