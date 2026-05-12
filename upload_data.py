from pymongo.mongo_client import MongoClient
import pandas as pd
import json

uri="mongodb+srv://taherali535251_db_user:Tupperware786@cluster0.eobina9.mongodb.net/?appName=Cluster0"

#create new client and connecct to server
client = MongoClient(uri)

#create a databasee and collection
databse_name = "pwskills"
collection_name = "wafer_fault"

df = pd.read_csv("C:\Users\TAHERALI\Downloads\Sensor.default\notebooks\wafer_23012020_041211.csv")
df= df.drop("Unnamed: 0",axis=1)
json_record = list(json.loads(df.T.to_json()).values())
client[databse_name][collection_name].insert_many(json_record)