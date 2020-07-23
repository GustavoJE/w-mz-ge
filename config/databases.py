from pymongo import MongoClient 
import os

"""
Database configurations
"""

client = MongoClient(os.getenv('MONGO_HOST', "mongodb://admin:admin@sitrack-shard-00-00-2dk0b.mongodb.net:27017/?replicaSet=sitrack-shard-0&ssl=true&authSource=admin")) 
mydatabase = client[os.getenv("MONGO_DATABASE", "sitrack")]
mycollection = mydatabase[os.getenv("MONGO_COLLECTION","sitracktest")]   
