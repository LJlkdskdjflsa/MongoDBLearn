import datetime

from env import mongodb_password
from pymongo import MongoClient


cluster = "mongodb+srv://test:"+mongodb_password+"@cluster0.5u3na.mongodb.net/test?retryWrites=true&w=majority"

client = MongoClient(cluster)

#print(client.list_database_names())

db = client.test
#print(db.list_collection_names())

todo1 = {
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

todos2 = [
  {
  "name": "lj1",
  "text": "myASDF first todo",
  "status": "open",
  "tags": [
    "python",
    "coding"
  ],
  "date": datetime.datetime.utcnow()
}
  ,
  {
  "name": "lj2",
  "text": "my 2 todo",
  "status": "close",
  "tags": [
    "JAVA",
    "coding"
  ],
  "date": datetime.datetime(2021,1,1,10,15)
}
]

#result = todos.insert_many(todos2)

#use collection to do things
#result = todos.find_one({"name":"lj1","text": "myASDF first todo"})

from bson.objectid import ObjectId
#result = todos.find_one({"_id":ObjectId("60a0d0550ae1b9473316cba9")})
results = todos.find({"name":"lj"})
print(list(results))

for result in results:
  print(result)