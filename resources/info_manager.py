from flask_restful import Resource, request
from models.database import DatabaseModel

class InfoManager(Resource):

  def post(self, target_name):
    data_received_by_request = request.get_data().decode('utf-8')

    save_in_database = DatabaseModel(target_name, data_received_by_request).save()

    # to fool
    return {"message": "The method is not allowed for the requested URL."}, 405
