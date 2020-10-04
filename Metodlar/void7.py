def harfSayici(giris):
    harfler = ["a","e","ı","i","o","ö","u","ü"]
    sesliler = 0
    sessizler = 0
    for i in giris:
        if i in harfler:
            sesliler +=1
        else:
            sessizler +=1
    print(f"Sesli harf sayısı: {sesliler}\nSessiz harf sayısı : {sessizler}")

metin = input("Lütfen metin giriniz: ").lower()

harfSayici(metin)