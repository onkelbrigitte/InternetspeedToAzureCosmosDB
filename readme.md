# InternetspeedToAzureCosmosDB

## Synopsis
This is a short script that determines your internet speed (upload, download, ping) and persists results in [Azure Cosmos DB](https://docs.microsoft.com/en-us/azure/cosmos-db/).

The reason I created this is that I encountered periodically networking issues when making video-calls over the internet and needed to analyse my connection quality on different machines with different connection types (WiFi vs. Ethernet). 

For measuring the internet speed/bandwidth, I am using the [speedtest-cli library](https://github.com/sivel/speedtest-cli), that is talking to the [speedtest.net](https://www.speedtest.net/) service. 

For the Azure Cosmos DB part, I am using the current (4.0.0 at the time creating this script) [Cosmos DB SDK](https://docs.microsoft.com/en-us/python/api/overview/azure/cosmos-readme?view=azure-python).

## To-Do
Error-handling is not happing at all, so this script is not as robust as it should be. I might add this at a later time.

## Usage
You need to create an Azure Cosmos DB instance using the SQL API and create a database as well as a container (a.k.a. collection). Provide this information in the config.json file using the sample that I created. 

Install the libraries `pip install speedtest-cli` and `pip install azure-cosmos` and run the script.