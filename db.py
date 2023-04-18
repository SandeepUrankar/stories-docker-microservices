from pymongo import MongoClient

def get_db():
    client = MongoClient(host='project_mongodb',
                         port=27017, 
                         username='root', 
                         password='pass',
                        authSource="admin")
    # db = client["animal_db"]
    db = client["project_db"]
    return db
