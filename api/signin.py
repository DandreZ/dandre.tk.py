from flask import Flask, request
import pymongo
@app.route('/signin', methods=['POST'])
def gethtml():
    name=request.form['name']
    password=request.form['password']
    print(name,password)
if __name__ == '__main__':
    app.run(debug=True)