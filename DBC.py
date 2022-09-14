from PyMongo import MongoClient


# create an instance (database connectivity)
Client = MongoClient("mongodb://127.0.0.1:27017")  # mandatory line to connect with database

Client.close()
