from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

load_dotenv()

uri = os.environ["URI"]
client = MongoClient(uri)

for dbname in client.list_database_names():
    print(dbname)

client.close()