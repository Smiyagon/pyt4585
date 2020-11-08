//Database oluşturma
use TelefonRehberi
//Tablo ekleme
db.Kisiler.insertMany([
    {
        "firstname": "Tarık",
        "lastname": "Kotan"
    },
    {
        "firstname": "Ahmet",
        "lastname": "Çebi"
    },
])


db.Telefonlar.insertMany([
    {
        "name": "work",
        "number": "+9021312684",
        "personId": ObjectId("5fa6998b45ae58b87e4d326d")
    },
    {
        "name": "home",
        "number": "+9021312684",
        "personId": ObjectId("5fa6998b45ae58b87e4d326d")
    },
    {
        "name": "cell",
        "number": "+9021312684",
        "personId": ObjectId("5fa6998b45ae58b87e4d326d")
    }
])


db.Kisiler.aggregate({
    $lookup: {
        from: "Telefonlar",
        localField: "_id",
        foreignField: "personId",
        as: "TelefonNumaralari"
    }
}).pretty()
db.Games.update({ "Id": 183 }, {
    $set: { "ImageUrl": "bilgeadam" }

db.Telefonlar.updateMany(
        { "number": "+9021312684" },
    { $set: { "personId": ObjectId("5fa6998b45ae58b87e4d326d") } }
    )