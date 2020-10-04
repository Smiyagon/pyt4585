# dışarıdan bir sayısal dizi alacak metot parametrede ki yer alan elemanların toplamının karekökünü geriye teslim etsin
import math

def sayılar(sayi1,sayi2):
    toplam = sayi1 + sayi2
    return print(math.sqrt(toplam))

sayi1 =int(input("Lütfen sayı giriniz : "))
sayi2 = int(input("Lütfen sayı giriniz : "))
sayılar(sayi1,sayi2)
