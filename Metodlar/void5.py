# Parametre alan metodlar

#Aldığı parametreye göre işlem seyrini değiştiren yapılardır
#1-)Kesinlikle metot içerisinde parametrenin nerden geleceği tanımlanmaz
#2-)Kesinlikle metod içerisinde parametreye değer atanmaz

# Dışarıdan alınan 2 sayıyı ekrana yazdıran metod

def hesapla(sayi1,sayi2):
    toplam = sayi1 + sayi2 
    print(toplam)

s1 = int(input("Sayı giriniz"))
s2 = int(input("Sayı giriniz"))

hesapla(s1,s2)
