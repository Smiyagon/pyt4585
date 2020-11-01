/*
1) show dbs           : server içerisinde yer alan database'leri görüntüler
2) use <databese adı> : çalışmak istediğiniz database'in adını vermeniz yeterlidir.Not : küçük,büyük harf duyarlılığı vardır.
3) show collections   : database içerisinde yer alan koleksiyonlar(table)'ı gösterir.
*/

// use kisiler => kisiler database'ini seçili hale getirdik




// 1) use TelefonRehberi => TelefonRehberi adında bir db oluşturduk
/* 2)
        db.Kisiler.insert({
            "firstname" : "cem",
            "lastname"  : "dalay",
            "mail"      : "cemdalay@outlook.com",
            "phone"     : "+905312837775",
            "phones"    :[
                {
                    "name":"is",
                    "phone": "+905312837777"
                },
                {
                    "name":"ev",
                    "phone": "+905312837778"
                },
                {
                    "name":"okul",
                    "phone": "+905312837779"
                }
            ]
        })
*/

// 3) db.Kisiler.find()
// 4) db.Kisiler.find().pretty()