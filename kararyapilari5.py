# mantıksal operatörler

# and sorguya katılan her bir koşulun sağlanması durumu
# or sorguya katılan koşullardan herhangi birinin sağlanması yeterlidir
# not sorguya olumsuzluk katar, değil ise anlamı taşır

# username = input("lütfen kullanıcı adınızı giriniz: ")
# if(username == "admin"):
#     password = input("lütfen şifrenizi giriniz : ")
#     if password == "123456":
#         print("giriş yaptınız")
#     else:
#         print("Kullanıcı bilgilerinizi kontrol ediniz")
# else:
#     print("Kullanıcı bilgilerinizi kontrol ediniz")



# username = input("Lütfen kullanıcı adınızı giriniz")
# password  = input("Lütfen şifrenizi giriniz")
# if username == "admin" and password == "123":
#     print("tebrikler giriş yaptınız")
# else:
#     print("Kullanıcı bilgilerinizi kontrol ediniz")

# örnek
def notlar():
    _not = int(input("Notunuzu giriniz : "))

    if (_not >= 0) and (_not <= 30):
        print(f"Notunuz: {_not} = FF")
    elif (_not >= 31) and (_not <= 50):
        print(f"Notunuz: {_not} = DD")
    elif (_not >= 51) and (_not <= 70):
        print(f"Notunuz: {_not} = CC")
    elif (_not >= 71) and (_not <= 84):
        print(f"Notunuz: {_not} = BB")
    elif (_not >= 85) and (_not <= 100):
        print(f"Notunuz: {_not} = AA")
    else:
        print("Lütfen 0 ile 100 arasında bir değer giriniz")

def urunler():
    try:
        urunadi = input("Ürün adını giriniz: ").lower().replace(" ","")
        if urunadi == "domates" or urunadi == "biber"  or urunadi == "patlıcan":
            print("Sebze Reyonu")
        elif urunadi == "şampuan" or urunadi == "parfüm"  or urunadi == "deodorant":
            print("Kozmetik Reyonu")
        elif urunadi == "ceptelefonu" or urunadi == "televizyon"  or urunadi == "bilgisayar":
            print("Teknoloji Reyonu")
        else:
            print("Bu ürün bizde bulunmamaktadır.")
    except:
        print("Lütfen ürün adını doğru giriniz")

def kitap():
    try:
        adet = int(input("Kitap adedini giriniz: "))
        fiyat = 5
        if adet < 0 :
            print("Lütfen düzgün değer giriniz.")
        elif adet >=1 and adet <= 20:
            print(f"Tebrikler %5 indirim kazandınız ödiyeceğiniz fiyat : {(fiyat*adet)-((fiyat * adet)*0.05)}")
        elif adet >=21 and adet <= 50:
            print(f"Tebrikler %10 indirim kazandınız ödiyeceğiniz fiyat : {(fiyat*adet)-(fiyat * adet)*0.10}")
        elif adet >=51 and adet <= 80:
            print(f"Tebrikler %15 indirim kazandınız ödiyeceğiniz fiyat : {(fiyat*adet)-(fiyat * adet)*0.15}")
        elif adet >=81 and adet <= 100:
            print(f"Tebrikler %20 indirim kazandınız ödiyeceğiniz fiyat : {(fiyat*adet)-(fiyat * adet)*0.20}")
        elif adet > 100 :
            print(f"Tebrikler %25 indirim kazandınız ödiyeceğiniz fiyat : {(fiyat*adet)-(fiyat * adet)*0.25}")
        else:
            print("Lütfen sayısal bir değer giriniz")
    except:
        print("Lütfen sayısal değer giriniz!!!")

urunler()