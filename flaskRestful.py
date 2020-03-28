from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {"about" : "Hello World from Martha Spitz"}
    def post(self):
        some_json = request.get_json()
        return {"you posted": some_json}, 201

class MultiByTen(Resource):
    def get(self, num):
        return {"result": num * 10}

api.add_resource(HelloWorld, "/")
api.add_resource(MultiByTen,"/multi/<int:num>")

if __name__ == '__main__':
    app.run(debug=True)