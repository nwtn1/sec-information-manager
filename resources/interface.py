from flask import render_template, make_response
from flask_restful import Resource, request
from models.database import DatabaseModel
class Interface(Resource):
  def get(self, secret_key):
    if secret_key == "admin":
      data_list = DatabaseModel.find_all()
      return make_response(render_template("dashboard.html", data_list=data_list), 200)
    return make_response(render_template("error.html", title='404 Not Found'))