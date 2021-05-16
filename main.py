import datetime

from env import mongodb_password
from pymongo import MongoClient


cluster = "mongodb+srv://test:"+mongodb_password+"@cluster0.5u3na.mongodb.net/test?retryWrites=true&w=majority"

client = MongoClient(cluster)

#print(client.list_database_names())

db = client.test
#print(db.list_collection_names())

todo1 = {
  "_id": 1,
  "name": "lj",
  "text": "my first todo",
  "status": "open",
  "tags": [
    "python",
    "coding"
  ],
  "date": datetime.datetime.utcnow()
}

todos = db.todos
#result = todos.insert_one(todo1)


