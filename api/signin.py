from flask import Flask, request
import pymongo


app = Flask(__name__)
@app.route('/signin', methods=["POST","GET"])
def gethtml():
    name=request.form['name']
    email=request.form['email']
    password=request.form['password']
    print(name,email,password)
    print('q')
if __name__ == '__main__':
    app.run()
AllClient=pymongo.MongoClient('mongodb+srv://root:dzr090315@dandre.g6y0ihm.mongodb.net/')
UserDB=AllClient['user']
UserCol=UserDB['account']
NewAcc={"name":"%s","email":"%s","password":"%s"}
UserCol.insert_one(NewAcc)