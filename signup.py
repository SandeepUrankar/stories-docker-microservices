from flask import Flask, jsonify, request
import db

app = Flask(__name__)


def get_db():
    """
    This method returns the instance of mongodb.
    """
    return db.get_db()


@app.route('/get-all-users')
def get_users():
    """ 
    
    This method fetches all the data about the user from mongodb.
    """
    # db=""
    try:
        _db = get_db()
        _users = _db.users.find()
        users = [{"id": user["id"], "name": user["name"],
                  "pass": user["pass"]} for user in _users]
        return jsonify({"users": users})
    except Exception:
        return jsonify({"message": "Error while fetching"})
    # finally:
    #     if isinstance(db)==MongoClient:
    #         db.close()


@app.route('/signup', methods=['POST'])
def signup():
    '''
    Method which creates a new user.
    '''
    data = request.json
    username = data['username']
    password = data['password']
    _db = get_db()
    _users = _db['users'].find()
    users = [{"id": user["_id"], "username": user["username"], "password": user["password"]} for user in _users]
    for user in users:
        if user['username'] == username:
            return jsonify({'message': f'User with {username} already exists.'})
    user = {"username": username, "password": password, "history": []}
    users = _db.users
    users.insert_one(user)
    return jsonify({"message": f'User with {username} created.'})


def main():
    '''
    Main method which runs the Flask app.
    '''
    app.run(host='0.0.0.0', port=3001)


if __name__ == '__main__':
    main()
