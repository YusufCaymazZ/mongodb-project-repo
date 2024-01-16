import os
import datetime
from PIL import Image

from dotenv import load_dotenv
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



class Addition:
    def __init__(self = None,db_name='iris_pics', collection_name='iris'):
        #load_dotenv()
        #self.MONGODB_URI = os.environ["URI"]
        self.client = MongoClient("mongodb+srv://DartVaderxd:yscymz@iris.n6xfz7x.mongodb.net/?retryWrites=true&w=majority")
        self.db = self.client[db_name]
        self.fs = GridFS(self.db, collection=collection_name)
    def save_image(self,image_path):
        # Görseli GridFS kullanarak MongoDB'ye ekle
        with open(image_path, 'rb') as image_file:
            # Görseli GridFS kullanarak MongoDB'ye ekle
            image_id = self.fs.put(image_file, filename=image_path)
            return image_id
    
    def get_image(self, image_id):
        # Belirtilen ObjectId ile görseli MongoDB'den al
        image_data = self.fs.get(ObjectId(image_id)).read()
        return image_data


    def display_image(self,image_id):
        # Belirtilen ObjectId ile görseli MongoDB'den al ve ekrana göster
        image_data = self.get_image(image_id)
        img = Image.open(io.BytesIO(image_data))
        img.show()
    

image_handler = Addition()
# Görseli MongoDB'ye ekle
uploaded_image_id = image_handler.save_image('iris\iris-setosa\iris-0c826b6f4648edf507e0cafdab53712bb6fd1f04dab453cee8db774a728dd640.jpg')
print(f'Uploaded Image ID: {uploaded_image_id}')

# MongoDB'den alınan görseli ekrana göster
image_handler.display_image(uploaded_image_id)

print("File one executed when imported")