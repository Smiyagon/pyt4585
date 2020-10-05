#1-) dışarıdan aldığı değere göre içi boş kare çizen metod yazınız : 
#2-) 1 ile 10 arasındaki sayıları çarpım tablosu olarak yazrıdan metod yazınız 

#format => 
# 1 x 1 = 1
#----------
# 2 x 2 = 4


def kare(sayi):
    for i in range(sayi):
        for a in range(sayi):
            if (i == 0 or i == sayi - 1) or (a == 0 or a== sayi-1) :
                print("*", end = " ")
            else:
                print(" " , end= " ")
        print()

sayi = int(input("değer giriniz : "))

kare(sayi)


def carpimTablosu(sayi):
    print("Çarpım Tablosu", sayi)
    for i in range(0, 11):
        print("------------------")
        print(sayi,"X",i,"=",sayi * i)

sayi = int(input("Sayı Giriniz: "))
carpimTablosu(sayi)