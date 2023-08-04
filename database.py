from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
load_dotenv()
username = os.getenv('temp_user')
password = os.getenv('passkey')

#class to initialize the database connection
class database():
        def __init__(self):
            self.uri = f"mongodb+srv://{username}:{password}@testing.mzq6q3n.mongodb.net/?retryWrites=true&w=majority"
            self.client = MongoClient(self.uri, server_api=ServerApi('1'))
            try:
                self.client.admin.command('ping')
            except Exception as e:
                print(e)

            self.db = self.client["Corider"]
            self.collection = self.db['User_data']
            

#returns the data contained by the pymongo cursor
def get_list(cursor):
    data_list=[]
    for i in cursor:
        del i['_id']
        data_list.append(i)
    if len(data_list)==1:
        return data_list[0]
    return data_list