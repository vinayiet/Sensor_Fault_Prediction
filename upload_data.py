# username : vinayiet password: 1234
# mongodb+srv://vinayiet:1234@cluster0.tfuy8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0

from pymongo.mongo_client import MongoClient
import pandas as pd
import json
from constant import MONGO_DB_URL, MONGO_DATABASE_NAME, MONGO_COLLECTION_NAME


client = MongoClient(MONGO_DB_URL)
file_path = r'notebooks\wafer_23012020_041211.csv'
df = pd.read_csv(file_path)
df = df.drop('Unnamed: 0', axis=1)

json_record = list(json.loads(df.T.to_json()).values())
client[MONGO_DATABASE_NAME][MONGO_COLLECTION_NAME].insert_many(json_record)
