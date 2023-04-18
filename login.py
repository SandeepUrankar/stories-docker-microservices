from flask import Flask, jsonify, request
import pymongo
from pymongo import MongoClient
import db

app = Flask(__name__)


def get_db():
    # client = MongoClient(host='project_mongodb',
    #                      port=27017, 
    #                      username='root', 
    #                      password='pass',
    #                     authSource="admin")
    # # db = client["animal_db"]
    # db = client["project_db"]
    return db.get_db()


@app.route('/')
def ping():
    return "Hello"

@app.route('/get-all-users', methods=['GET'])
def get_users():
    db=None
    try:
        post = {"name": "sandeep", "pass":"Sandeep@123"}
        db = get_db()
        # users_collection = db.users
        # user_id = users_collection.insert_one(post)
        # db['users'].insert_one(post)
        _users = db['users'].find_one()
        # users = [{"id": user["_id"], "name": user["name"], "pass": user["pass"]} for user in _users]
        db.close()
        return jsonify({"users":_users})
    except:
        pass


@app.route('/login',methods=['POST'])
def login():
    data = request.json
    db = get_db()
    _users = db['users'].find()
    users = [{"id": user["_id"], "name": user["user"], "pass": user["pass"]} for user in _users]
    msg = "User not found."
    for user in users:
        if user["name"] == data['username']:
            if user['pass'] == data['password']:
                msg = "Login Success."
            else:
                msg = "Wrong password."
    if db == MongoClient:
        db.close()
    return jsonify({"message": msg})


def main():
    app.run(host='0.0.0.0', port=3000)

if __name__ == '__main__':
    main()