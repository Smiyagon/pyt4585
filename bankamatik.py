class Bankamatik(bakiyeSorgulama,paraCekme,paraEkleme):
    
    bakiye = 15000
    deger = int(input("Lütfen bir işlem seçiniz. (1,2,3,4)"))
    
    print("""
    1-)Bakiye Sorgulama
    2-)Para ekleme 
    3-)Para çekme
    4-)Çıkış
        
    """)
    
    if deger == 1 : 
        bakiyeSorgulama()
    elif deger == 2 :
        paraEkleme()
    elif deger == 3: 
        paraCekme()
    elif deger == 4:
        exit
    else: 
        print("Salak saçma şeyler deneme düzgün değerler gir.")
    

def bakiyeSorgulama():
    print(f"Bakiyeniz: {bakiye} Türk Liranız Var.")


def paraEkleme():
    eklenenPara = int(input("Ne kadar Para Yükleyeceksiniz: "))
    print(f"{eklenenPara + bakiye} Yeni bakiyeniz.")

def paraCekme():
    cekilenPara = int(input("Ne kadar Para cekiceksiniz : "))
    print(f"{bakiye - cekilenPara} Güncel Hesabınızda kalan para ")
        
        











