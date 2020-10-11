
def ascii(metin):
    toplam = 0
    for i in metin:
        a = int(ord(i))
        toplam += a
    print(f"Girdiğiniz metnin ascii değerleri toplamı:{toplam}")

metin = input("Lütfen metin giriniz: ")
ascii(metin)


file1 = "ba.png"
file2 = "ba.jpg"
file3 = "ba.gif"
file4 = "ba.png"
file5 = "ba.tff"
file6 = "ba.mp3"
file7 = "ba.mp4"
file8 = "ba.jpg"
file9 = "ba.gif"
file10 = "ba.png"
file11 = "ba.gif"


def dosyalar(*liste):
    toplam = 0
    for i in liste:
        if ".png" in i:
            toplam += 1
    return toplam
liste = dosyalar(file1,file2,file3,file4,file5,file6,file7,file8,file9)

print(f".png olan dosya sayısı : ",liste)