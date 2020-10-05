# kullanıcı dışarıdan sayısal olarak bir dizi gönderecek, siz bunu sayısal diziye çeviren bir metot yazınız.


#  3 4 5 6 7 8 9 0 d aa sdd =>[3,4,5,6,7,8,9.9,11,]


def donustrucu(dizi):
    liste = dizi.split()
    for harf in range(len(liste)):
        if liste[harf].count("."):
            liste[harf] = float(liste[harf])
        else:
            liste[harf] = str(liste[harf])
        
    return liste

sonuc = donustrucu("3 5 1  21  21.4 asd a")
print(sonuc)