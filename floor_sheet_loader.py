import pandas as pd
import pymongo

def load_from_csv(path):
    return pd.read_csv(path)

def load_from_mongo(uri, db_name, collection):
    client = pymongo.MongoClient(uri)
    db = client[db_name]
    data = pd.DataFrame(list(db[collection].find()))
    return data