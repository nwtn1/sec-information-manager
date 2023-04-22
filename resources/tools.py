from flask_restful import Resource, request

class InfoManager(Resource):
  def post(self, target_name):
    return target_name