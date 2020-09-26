# birden fazla elemanla çalışacak isek tek tek değişken tanımlamak yerine dizi kullanıyoruz
# tanımlama şekli

sehirler = ["istanbul", "edirne",  "ankara", "rize" ,"kayseri","malatya"]
#Not : Bir dizinin index değeri , o dizinin eleman sayısı (uzunluğu) 1- değeridir
                #eleman sayı => 6
                #index değeri => 5


print(sehirler[0]) # dizinin ilk elemanı ekrana yansıtılır


#dizinin son elemanını ekrana yazdırınız
index = len(sehirler) - 1
print(sehirler[index])

print(sehirler[2:5]) # 1. parametrede verilen index değerinden başlar 2. parametrede verilen ise index değerinin bir alt değerine kadar olan elemanları listeler


# dizinin tüm elemanlarını ekrana yazdırmak istersek 
print(sehirler[:])

print("edirne" in sehirler)  # edirne parametresi dizi içerisnde geçiyor mu geçmiyor mu

# örnek 



# if giris in sehirler:    
#     print("vardır") 
# else:    
#     print("yoktur")

giris = input("Şehir adı giriniz : ")

result = f"parametrede gönderdiğiniz {giris} yer almaktadır" if giris in  sehirler else  f"parametrede gönderdiğiniz {giris} yer almamaktadır"

print("parametrede gönderdiğiniz {} yer alma{}ktadır" .format(giris,((""if giris in  sehirler else  "ma"))))

print(result)

myList1 = ["sehirler dizisi"]
print(myList1)

myList2 = ["arabalar dizisi"]
print(myList2)

myList3 = ["renkler dizisi"]
print(myList3)


result = list(zip(myList1,myList2,myList3))
print(result)