from datetime import datetime
from json import dumps, loads

class FileManager():

  def __init__(self, data_origin, data_to_write):
    self.data_origin = data_origin
    self.data_to_write = data_to_write
    self.current_data_in_file = []


  def organize_to_json(self):

    data_reception_time = datetime.now().strftime("%m/%d/%y %H:%M")

    data_as_dictionary = {
      "origin": self.data_origin,
      "token": self.data_to_write,
      "receiveAt": data_reception_time
    }

    self.current_data_in_file.append(data_as_dictionary)
    self.data_to_write = self.current_data_in_file


  def read_text_in_file(self):
    try:
      with open("./data.json", "r+") as json_file:
        self.current_data_in_file = loads(json_file.read())
    except:
      self.current_data_in_file = []


  def write_text_in_file(self):

    self.read_text_in_file()
    self.organize_to_json()

    print(self.data_to_write)

    with open("./data.json", "w+") as json_file:
      json_file.write(dumps(self.data_to_write, indent=2))