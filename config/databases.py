from pymongo import MongoClient 
import os

"""
Database configurations
"""

<<<<<<< HEAD
client = MongoClient(os.getenv('MONGO_HOST', "mongodb://admin:gje150689@sitrack-shard-00-00-2dk0b.mongodb.net:27017/?replicaSet=sitrack-shard-0&ssl=true&authSource=admin")) 
mydatabase = client[os.getenv("MONGO_DATABASE", "Smarted")]
mycollection = mydatabase[os.getenv("MONGO_COLLECTION","Smartedexam")]   
=======
client = MongoClient(os.getenv('MONGO_HOST', "mongodb://admin:admin@localhost")) 
mydatabase = client[os.getenv("MONGO_DATABASE", "")]
mycollection = mydatabase[os.getenv("MONGO_COLLECTION","")]   
>>>>>>> bf4bdba1fed8dc0292a53aad13ad5ef9054cfa80
