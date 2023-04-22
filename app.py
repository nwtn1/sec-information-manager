from flask import Flask, render_template
from flask_restful import Api

from resources.info_manager import InfoManager
from resources.interface import Interface

from sql_alchemy import db

app = Flask(__name__, template_folder="./templates")
api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.db"

@app.before_first_request
def create_db():
    db.create_all()

db.init_app(app)

api.add_resource(InfoManager, "/receive/<target_name>")
api.add_resource(Interface, "/show/<secret_key>")


if __name__ == '__main__':
  app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=True)
