from pymongo import MongoClient 
import os

"""
Database configurations
"""

client = MongoClient(os.getenv('MONGO_HOST', "mongodb://admin:admin@localhost/")) 
mydatabase = client[os.getenv("MONGO_DATABASE", "")]
mycollection = mydatabase[os.getenv("MONGO_COLLECTION","")]   
