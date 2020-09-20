
try:
    sayi1 = int(input("Sayı giriniz: "))
    if sayi1%2 == 0:
        print("Sayı çifttir")
    else:
        print("sayı tektir")
except:
    print("Sayısal değer giriniz")