metin = input("Lütfen bir metin giriniz : ")

sesli_harfler = ["a","e","ı","i","o","ö","u","ü"]
sesliler = []
sessizler = []
i= 0

while i <len(metin):
    if sesli_harfler.count(metin[i]):
        sesliler.append(metin[i])
    else:
        sessizler.append(metin[i])
    i+= 1

print(f"Metindeki sesli harf sayısı : {len(sesliler)}\nMetindeki sessiz harf sayısı : {len(sessizler)}")