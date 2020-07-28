import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

"""
Application configurations
"""

config = {
    "port": os.getenv("APP_PORT",8000),
    "debug": os.getenv("APP_DEBUG",False),
    "secret-key": os.getenv("APP_SECRET_KEY")
}

