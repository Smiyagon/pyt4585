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