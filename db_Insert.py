import pymongo
import json
import os

files = ['Higher_temb_obs', 'Last_Year_Measurement', 'stations']

conn = os.environ.get("MONGODB_URI")

client = pymongo.MongoClient(conn)
db = client.videogames
collection = db.surfer_climate

for file in files:
    with open('/Users/enriquevazquez/Documents/BootCamp TEC/Bootcamp Program/?TDM-REV-DATA-PT-01-2020-U-C/02-Homework/10-Advanced-Data-Storage-and-Retrieval/SQLAlchemy-Challenge/Resources/' + file + '.json', 'r') as myfile:
        data = myfile.read()
    obj = json.loads(data)
    dict = {'data': obj}
    collection.insert_one(dict)