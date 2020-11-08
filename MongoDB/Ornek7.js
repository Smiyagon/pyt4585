db.Categories.aggregate({//Ana tabloyu ağırıyoruz.
    $lookup:{
        from:"Products",//Join yapılacak tablo
        localfield : "_id", //ana tablo içerisinde yer alan primary key
        foreignField :"CategoryID", //ForeignKey ikincil alan,ürünler tablosunda Kategoriyi temsil eden alan
        as:"Products" //sorgu sonucu kategoriye bağlı ürünler listelenirken verilecek olan isim (opsiyonel)
    }
})

db.Categories.aggregate({
    $lookup:{
        from:"Products",
        localField : "CategoryID", 
        foreignField :"CategoryID", 
        as:"Products" 
    }
}).pretty()