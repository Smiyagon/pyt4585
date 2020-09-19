
print("Merhaba")


# degisken tanimlama kurallari
# 1) degiskenin ismi sayi ile baslayamaz
# 2) degisken , iki veya daha fazla kelimeden olusamaz , olusucaksa bile araya _ kullanilir
# 3) degisken tanimlamasi yapilirken , kesinlikle tanimli kelimeler kullanilamaz
# 4) degisken adinda lutfen rica ediyorum , turkce karakter kullanmayiniz.


hocanin_adi = "murat vuranok"
hocanin_mail_adresim = "murat.vuranok@bilgeadam.com"
adim = "Tarik"
soyadim = "Kotan"

#int  , string , float

sayi = 5 # int tam sayi veri tipi
print(type(sayi))

sayi2 = 3.13
print(type(sayi2))

yazi = "String"

print(type(yazi))


print(adim + " " + soyadim + "\n Hocanin adi:" + hocanin_adi)  # \n bir alt satıra geç
print(adim,soyadim)

x= True
y= False

print(x)
print(y)

print(type(x))

print((hocanin_adi+ "\n")*5)

print("""
Tarık
Kotan
Bilge Adam
""")

print("bilge adam \"beşiktaş\" yazılım dersleri istanbul\n\
    python kursu\
    test satırı")


