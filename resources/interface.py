from flask_restful import Resource, request
from tools.file_manager import FileManager
class Interface(Resource):
  def get(self):
    file_manager = FileManager()
    file_manager.read_text_in_file()
    return file_manager.current_data_in_file