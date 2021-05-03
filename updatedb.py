import sys
from datetime import datetime, timedelta
from pymongo.collection import ReturnDocument

from pymongo import MongoClient

MONGODB_STRING = 'mongodb+srv://thomashedgepath:2WuK7XUKEpPRAeopNgTQPjjdm6K@ccc-properties-sy4of.gcp.mongodb.net/'
DB_NAME = 'properties'
COLLECTION_NAME = 'map-layers'


client = MongoClient(MONGODB_STRING)
db = client[DB_NAME]
#collection = db[COLLECTION_NAME]


def update_db(source_url, file_path="", display_name="", layer_group="", metadata_map="", style=""):
    # display_name = ""
    # layer_group = ""
    # metadata_map = ""
    # style = ""

    pass
    update = {
                "$currentDate": {"lastModified": True},
                "$set": { 
                    "original_source": source_url,
                    "display_name": display_name,
                    "layer_group": layer_group,
                    "metadata_map": metadata_map,
                    "style": style
                }
            }

    query = { "original_source": source_url }
    new = db["map-layers"].find_one_and_update(query,update,upsert=True,return_document=ReturnDocument.AFTER)

    #print(new)


source_url = input("Source URL: ")
display_name = input("Display Name: ")
layer_group = input("Layer Group: ")
# metadata_map = ""
# style = ""

update_db(source_url, display_name, layer_group)

another = input("Add another?")

while another == 'y' or 'Y':
    source_url = input("Source URL: ")
    display_name = input("Display Name: ")
    layer_group = input("Layer Group: ")
    # metadata_map = ""
    # style = ""

    update_db(source_url, display_name, layer_group)
    another = input("Add another?")

