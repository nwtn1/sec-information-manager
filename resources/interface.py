from flask import render_template, make_response
from flask_restful import Resource, request
from models.database import DatabaseModel
class Interface(Resource):

  def get(self, secret_key):
    if secret_key == "admin":
      data_list = DatabaseModel.find_all()
      data_list = sorted([data.as_json() for data in data_list], key=lambda k: k["id"], reverse=True)
      return make_response(render_template("dashboard.html", data_list=data_list), 200)

    return make_response(render_template("error.html"))