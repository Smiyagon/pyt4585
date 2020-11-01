// Equality == 
// db.Products.find({"ProductID":77})    => ürün id değeri 77 olan kaydı getirir


// db.Products.find({"CategoryID":8})

// 
// Fıyatı 50 dolardan az olan ürünlerin listelenmesi : 

db.Products.find({"UnitPrice": {$lt:50} }).pretty()


// ürünlerin sıralanması:
// Ascending => +1 A'dan Z'ye 0 dan 9'a sıralama yapar (Küçükten büyüğe)
// Descending => -1 Z'den A'ya 9'dan 0'a sıralama yapar (Büyükten küçüğe)

// db.Products.find().pretty().sort({"UnitPrice":1}) => Ascending
// db.Products.find().pretty().sort({"UnitPrice":-1}) => Descending

// less than equal 
// Fiyatı 50$ eşit veya küçük olan ürünlerin küçükten büyüğe sıralanması;

db.Products.find({"UnitPrice":{$lte:50}}).pretty().sort({"UnitPrice":1})


// greater than >

db.Products.find({"UnitPrice":{$gt:100}}).pretty().sort({"UnitPrice" :1})


// greater than equal

db.Products.find({"UnitPrice":{$gte:60}}).pretty().sort({"UnitPrice" :1})