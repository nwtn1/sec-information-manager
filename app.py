from flask import Flask
from flask_restful import Api, request, Resource


app = Flask(__name__)
api = Api(app)

@app.before_request
def before_request():
  return ""


if __name__ == '__main__':
  app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=True)
