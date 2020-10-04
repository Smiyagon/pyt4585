def oyunlar(isim,soyisim):
    isim = isim[0:2].upper()+isim[2:].lower()    
    soyisim = soyisim.replace("a","e")
    sonuc = print(f"{isim}.{soyisim}@hotmail.com")
    return sonuc

isim = input("Lütfen isim giriniz:  ")
soyisim =input("Lütfen Soyisim giriniz : ")
oyunlar(isim,soyisim)
