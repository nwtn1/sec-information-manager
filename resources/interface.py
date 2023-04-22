from flask_restful import Resource, request
from models.database import DatabaseModel
class Interface(Resource):
  def get(self):
    data_list = DatabaseModel.find_all()
    return [data.as_json() for data in data_list]