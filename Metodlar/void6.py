
def metod(isim,soyisim = None):
    if soyisim == None:
        print(f"{isim}@hotmail.com")
    else:
        print(f"{isim}.{soyisim}@hotmail.com")

isim  = input("Lütfen adınızı giriniz : ")
soyisim = input("Lütfen soyadınızı giriniz : ")

metod(isim,)