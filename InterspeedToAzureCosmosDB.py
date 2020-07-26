import json
import speedtest
import uuid
from azure.cosmos import exceptions, CosmosClient

#read config file
config = json.loads(open('config.json','r').read())

#Azure CosmosDB connection details and further config
cosmosdb_url = config["cosmosdb_url"]
cosmosdb_key = config["cosmosdb_key"]
cosmosdb_db = config["cosmosdb_db"]
cosmosdb_collection = config["cosmosdb_collection"]
connectionType = config["connectionType"]

#test internetspeed
speed = speedtest.Speedtest()
speed.get_best_server()
speed.download()
speed.upload()

result = speed.results.dict()

#add connection type and generated ID (required by Azure CosmosDB) to result JSON doc
result["connectionType"] = connectionType
result["id"] = str(uuid.uuid4())

#Connect to Azure CosmosDB and write document
cosmosclient =  CosmosClient(cosmosdb_url, cosmosdb_key) \
               .get_database_client(cosmosdb_db) \
               .get_container_client(cosmosdb_collection) \

cosmosdbResponse = cosmosclient.create_item(body=result)


                

