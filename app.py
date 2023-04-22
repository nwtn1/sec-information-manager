from flask import Flask
from flask_restful import Api

from resources.tools import InfoManager
from resources.interface import Interface

app = Flask(__name__)
api = Api(app)

api.add_resource(InfoManager, "/receive/<target_name>")
api.add_resource(Interface, "/show")


if __name__ == '__main__':
  app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=True)
