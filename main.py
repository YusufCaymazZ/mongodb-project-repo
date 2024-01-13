import os
import datetime
from PIL import Image

from gridfs import GridFS
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo
from bson import ObjectId
import pprint
from pymongo.errors import OperationFailure

import pandas 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


load_dotenv()
MONGODB_URI = os.environ["URI"]
# Create a new client and connect to the server
client = MongoClient(MONGODB_URI)



class Addition:
    def __init__(self,path = None):
        self.path = path

    def Addition(self):
        pass



