from pymongo import MongoClient 
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

"""
Database configurations
"""

client = MongoClient(os.getenv("MONGO_URI", "mongodb://admin:admin@localhost:27017/")) 
mydatabase = client[os.getenv("MONGO_DATABASE")]
mycollection = mydatabase[os.getenv("MONGO_COLLECTION")]   

