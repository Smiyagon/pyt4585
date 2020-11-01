// var olan bir database'i silme 
// use <database ismi> 
// db.dropDatabase() => bulunduğun database'i siler.

// db içerisinde yer alan kayıtları listelemek için öncelikle database'in  seçilmiş olması gerekir.

// 1) use theatre
//      1.1) use Theatres
// 2) Database içerisinde yer alan collection'ın listelenmesi
//      2.1)db.Games.find() => tüm kayıtları listeler
//      2.2)db.Games.find().pretty() => düzgün formatta listleleme yapar
// 3) Koleksiyon içerisinde yer alan bütün kayıtların filtrelenerek listelenmesi
//      3.1)db.Games.find({"key":"value"})
//      3.2)db.Games.find({"key":"value"}).pretty()



// 4) Update işlemi , bir kaydın belirli bir alanı veya tüm kayıtların belirli alanlarının değiştirilmesi işlemi
// 4.1) db.Games.update({"key":"value"},{$set:{"key":"value"}})
//      1. Süslü parantez içeriği
// {kwt => filtreleme yaparken neye göre yapacaksınız propert adı: value => filtreleme yaparken verdiğiniz değer}
//      2. süslü parantez içeriği
// {$set : => eşitle anlamına gellir{key => hangi alan değişicek : value => o alanın yani değeri nedir?}}

// Ornek : db.Games.update({"Name":"12. GECE"},{$set:{"ImageUrl": "bilgeadam"}})

// db.Games.find({"Name":"12. GECE"}).pretty()

db.Games.update({"Id":1},{$set:{"ImageUrl":"bilgeadam"}})
db.Games.update({"Id":4},{$set:{"ImageUrl":"bilgeadam"}})
db.Games.update({"Id":180},{$set:{"ImageUrl":"bilgeadam"}})
db.Games.update({"Id":183},{$set:{"ImageUrl":"bilgeadam"}})


// db.Games.updateMany({"ImageUrl":"bilgeadam"},{$set:{"Url":"www.bilgeadam.com"}}) => Image urlsi bilgeadam olan bütün kayıtları www.bilgeadam.com olarak değiştirir

db.Games.find({"Url":"www.bilgeadam.com"}).pretty()


// var games = db.Games.find() => oyun listesini değişkene atadık.
// games.hasNext() => true dönüyorsa, içeride okunacak kayıt var anlamına gelir.