import pymongo
from Person import Person
from bson import ObjectId

# print(myClient.list_database_names())
__DATABASE_NAME = "PhoneBookDB"
__COLLECTION_NAME = "People"

def ConnectAtlas():
    return pymongo.MongoClient('mongodb+srv://Tarik:Password1@cluster0.9hqav.mongodb.net/PhoneBookDB?retryWrites=true&w=majority')

def Add(person):
    myClient = ConnectAtlas()
    myDb = myClient[__DATABASE_NAME]
    myCollection = myDb[__COLLECTION_NAME]
    myCollection.insert_one(person.__dict__)


def Delete(param):
    myClient = ConnectAtlas()
    myDb = myClient[__DATABASE_NAME]
    myCollection = myDb[__COLLECTION_NAME]
    query = {"_id" : ObjectId(param)}
    myCollection.delete_one(query)

def Show():
    myClient = ConnectAtlas()
    myDb = myClient[__DATABASE_NAME]
    myCollection = myDb[__COLLECTION_NAME]
    print(f"{'ID':30}        {'FIRSTNAME':14}        {'LASTNAME':18}         {'PHONE':27}      {'MAIL'}")
    print("-"*200)
    for p in myCollection.find():
        print(f"{p['_id']}              {p['FirstName']:15}       {p['LastName']:20}       {p['Phone']:25}        {p['Mail']:30}")
    print("-"*200)
        
def Update():
    myClient = ConnectAtlas()
    myDb = myClient[__DATABASE_NAME]
    myCollection = myDb[__COLLECTION_NAME]

    for x in myCollection.find():
        if x == id:
            
