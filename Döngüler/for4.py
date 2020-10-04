

for i in range(3):
    sifre =input("Lütfen şifrenizi giriniz: ")
    if len(sifre) in range(3,8):
        print(f"Şifreniz {sifre} olarak belirlenmiştir")
        break
    elif i == 2:
        print("3 kere yanlış girdin aptal")
    elif len(sifre) < 3 or len(sifre) >8:
        print("Lütfen 3 ile 8 karakter uzunluğunda bir şifre belirleyiniz.")



