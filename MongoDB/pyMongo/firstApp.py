import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

myDb = client["Northwind"]
myCollection = myDb["Products"]


products =myCollection.find({})
for x in products:
    print(x)