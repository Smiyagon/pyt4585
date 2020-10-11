def metot(**param):
    print("*"*45)
    for key,value in param.items():
        print("{:8} : {}".format(key,value))
    print("*"*45)


metot(
    Ad = "tarık",
    Soyad ="kotan",
    Telefon = "095664654",
    Mail = "tarik.kotan@hotmail.com"
)