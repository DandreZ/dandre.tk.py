from flask import Flask, request
import pymongo

while True:
    app = Flask(__name__)
    @app.route('signin', methods=["POST","GET"])
    def gethtml():
        name=request.form['name']
        password=request.form['password']
        print(name,password)
    if __name__ == '__main__':
        app.run()
