import datetime
import pickle
from flask import Flask, jsonify, request


# Global Variables
global stories
stories = dict()
global recos
recos = dict()
global categories
categories = set()
global app
app = Flask(__name__)


def load_data():
    '''
    This function loads the stories and their recommendations into the dict DS
    '''
    with open('files/saved_stories.pkl', 'rb') as f:
        global stories
        stories = pickle.load(f)
    with open('files/saved_recomendations.pkl', 'rb') as f:
        global recos
        recos = pickle.load(f)
    for i in stories.keys():
        global categories
        categories.add(stories[i]['Category'])
    categories = list(categories)

@app.route('/get-categories')
def get_categories():
    """
    Returns the categories of stories.
    """
    return jsonify({"categories" :  categories})

@app.route('/get-titles/<category>')
def get_story_titles(category):
    """
    Returns the titles of stories with selected category.
    """
    titles = []
    for i in stories.keys():
        if(stories[i]['Category'] == category):
            titles.append(stories[i]['Title'])
    return jsonify({"titles": titles})

@app.route('/get-all-stories')
def get_users():
    """ 
    This method fetches all the stories and returns.
    """


# @app.route('/signup', methods=['POST'])
# def signup():
#     '''
#     Method which creates a new user.
#     '''
#     data = request.json
#     username = data['username']
#     password = data['password']
#     user = {"user": username, "pass": password}
#     _db = get_db()
#     users = _db.users
#     users.insert_one(user)
#     return jsonify({"message": f'User with {username} created.'})


def main():
    '''
    Main method which runs the Flask app.
    '''
    load_data()
    app.run(host='0.0.0.0', port=3002)
    # get_categories()


if __name__ == '__main__':
    main()
