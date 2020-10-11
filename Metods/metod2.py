# dışarıdan gelecek olan parametre sayısı belirsiz olan durumlar için kullanılan metod tekniği

def hesapla(*sayilar):
    toplam = 0 
    for i in sayilar:
        toplam += i
    return toplam

result = hesapla(1,2,31,2)
print("toplama işlemi sonucu",result)