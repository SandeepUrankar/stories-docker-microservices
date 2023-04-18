from flask import Flask, jsonify, request
from pymongo import MongoClient
import db

app = Flask(__name__)


def get_db():
    return db.get_db()



@app.route('/get-all-users')
def get_users():
    db=""
    try:
        db = get_db()
        _users = db.users.find()
        users = [{"id": user["id"], "name": user["name"], "pass": user["pass"]} for user in _users]
        return jsonify({"users": users})
    except:
        pass
    finally:
        if type(db)==MongoClient:
            db.close()


@app.route('/signup',methods=['POST'])
def signup():
    data = request.json
    username = data['username']
    password = data['password']
    user = {"user":username, "pass": password}
    db = get_db()
    users = db.users
    users.insert_one(user)
    return jsonify({"message": f'User with {username} created.'})


def main():
    app.run(host='0.0.0.0', port=3001)

if __name__ == '__main__':
    main()