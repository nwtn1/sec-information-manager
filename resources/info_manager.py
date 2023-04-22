from flask_restful import Resource, request
from tools.file_manager import FileManager

class InfoManager(Resource):

  def post(self, target_name):
    data_received_by_request = request.get_data().decode('utf-8')

    file_manager = FileManager(target_name, data_received_by_request)
    file_manager.write_text_in_file()

    return "", 200
