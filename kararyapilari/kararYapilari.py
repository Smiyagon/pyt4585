#Kara Yapıları
# Karşılaştırma operatörleri 



# == (eşit eşittir) soldaki değerin sağdaki değere eşit olma durumudur
# 1 == 1 => true - if 
# 1 == 2 => false - else
num1 = int(input("1.SAYI : "))
num2 = int(input("2.SAYI : "))

if num1== num2:
    print("eşit")
else : 
    print("eşit değildir")

# != (eşit değildir ) soldaki değerin sağdaki değere eşit olmama durumu
# 1 !=1 => false- else 
# 2 ! = 1 => true - if

if num1 != num2:
    print("eşit değildir.")
else:
    print("eşittir")


# > (soldaki değerin sağdaki değerden büyük olma durumudur)
# 2 > 1 => true- if
# 1>1 => false - else

if num1 > num2 :
    print("1.sayı daha büyüktür")
else:
    print("2.Sayı daha büyüktür veya eşittir")


# < (soldaki değerin sağdaki değerden küçük olma durumudur)

# 1 < 2 => true - if
# 2 < 1 => false - else

if num1 < num2 :
    print("2. sayı daha büyüktür")
else: 
    print("1.sayı daha büyük veya eşittir")


# >= soldaki değerin sağdaki değerden büyük veya eşit olma durumudur

#  1 >=1 true - eşit olma - if
#  2 >=1 true - büyük olma - if
#  1 >=2 false - else

if num1 >= num2 : 
    print("1.sayı 2.sayıdan büyük veya eşittir")
else:
    print("2. sayı 1.sayıdan daha büyüktür")


# <= soldaki değerin sağdaki değerden küçük veya eşit olma durumu
# 1 <= 1 => true - eşit olma - if
# 1 <= 5 => true - küçük olma - if
# 5 <= 1 => false - else


if num1 <= num2:
    print("2.sayı 1.sayıdan büyük veya eşittir")
else:
    print("1.sayı 2. sayıdan büyüktür.")


username = input("Lütfen kullanıcı adınızı giriniz : ")
password = input("Lütfen şifreinizi giriniz : ")
username  = username.lower()\
.replace("ı","i")\
.replace("ö","o")\
.replace("ğ","g")\
.replace("ş","s")\
.replace("ü","u")\
.replace("ç","c")

print(username)


if (username == "admin") and (password == "admin"):
    print("tebrikler, giriş yaptınız.")
else: 
    print("Yanlış kullanıcı adı veya parola girdiniz.")