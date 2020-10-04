def tekCiftKontrol(sayi):
    if sayi == 0:
        return 0
    elif sayi % 2 == 0:
        return -1
    else:
        return 1
    

sayi = tekCiftKontrol(int(input("Lütfen sayı giriniz : ")))
print(sayi)