from env import mongodb_password
from pymongo import MongoClient


cluster = "mongodb+srv://test:"+mongodb_password+"@cluster0.5u3na.mongodb.net/test?retryWrites=true&w=majority"

client = MongoClient(cluster)

print(client.list_database_names())

db = client.test
print(db.list_collection_names())