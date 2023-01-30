from flask import Flask, request
import pymongo
name=1
while name==1:
    app = Flask(__name__)
    @app.route('/', methods=["POST"])
    def gethtml():
        global name
        global email
        global password
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        print(name,email,password)
        print('q')
        return "<p>sss<p>"
    if __name__ == '__main__':
        app.run()
        gethtml()
AllClient=pymongo.MongoClient('mongodb+srv://root:dzr090315@dandre.g6y0ihm.mongodb.net/')
UserDB=AllClient['user']
UserCol=UserDB['account']
NewAcc={"name":"%d"%(name),"email":"%d"%(email),"password":"%d"%(password)}
UserCol.insert_one(NewAcc)