import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

myDb = client["PhoneBook"]
myCollection = myDb["People"]
myCollection_phone = myDb["Phones"]



person={
    "firstname":"Tarık",
    "lastname" : "Kotan",
    "phone": "+645456456456",
    "mail":"tarik.kotan@hotmail.com"
}


# myCollection.insert_one(person)


# print(client.list_database_names()) => 
kisi_id = myCollection.insert_one(person).inserted_id
print(kisi_id) # 5fa6aa9e54f27beb4a1dcfac
people = myCollection.find({},{"phone":1,"firstname":1,"lastname":1,"_id":0})
for i in people:
    print("*"*40)
    for x,y in i.items():
        print(f"{x}:{y}")


phones = [{
    "name": "work",
    "phone" : "+6546512121",
    "personId": kisi_id
},
{
    "name": "home",
    "phone" : "+6546512121",
    "personId": kisi_id
},
{
    "name": "cell",
    "phone" : "+6546512121",
    "personId": kisi_id
}
]

myCollection_phone.insert_many(phones)
for p in myCollection.find():
    print("*"*40)
    print()
    for x,y in p.items():
        print(f"{x}:{y}")
    telefon_numaralari = myCollection_phone.find({"personId":p["_id"]})
    for t in telefon_numaralari:
        for c,d in t.items():
            print(f"{c}:{d}")
 