# Dizi üzerinde işlemler yapmak için o nesneye ait metodlar kullanılır

#.append() => dizi içerisine eleman eklemek için kullanılır.
#.append() => ekleme işlemini dizinin sonuna ekleyerek gerçekleştirir

sehirler = []

sehirler.append("ankara")

sehirler.append("edirne")

sehirler.append("istanbul")

print(sehirler)

#.insert() => dizi içerisinde belirli bir alana veri eklemek için kullanılır 
sehirler.insert(1,"bursa")
# 1. parametre dizinin hangi sırasına eleman eklenecek(index numarası veriniz )
# 2.parametre dizi içerisine eklenecek olan eleman


print(sehirler)



# .pop() => dizi içerisinden eleman silme, parametre verilir ise verilen index değerindeki elemanı , parametre verilmezse dizinin en son elemanını siler

#pop() => sildiği elemanı geriye teslim eder
print(sehirler)
sehirler.pop(2)
print(sehirler)
sehirler.pop()
print(sehirler)


########

arabalar = ["mercedes","bmw","range rover","bugatti" , "aston martin","tofaş","kartal","serçe"]

# .remove() => dizi içerisinden eleman silmekle mükellef diğer bir metodumuzdur , pop() metodundan farkı birisi index mekanizması üzerinden silme işlemi yaparken remove() object parametre alarak işlemedevam ederr
# dizi içersinde birden fazla aynı değer var ise , soldan sağa ilk bulduğu elemanı siler.
# remove metodu , pop metodu gibi silinen elemanı geriye teslim etmez void metottur.

print(arabalar)
print(arabalar.remove("tofaş"))
print(arabalar)

#-------------------------------------


#.sort() => dizi içerisinde yer alan elemanları a'dan z'ye - 0'dan 9'a sıralar

# print(arabalar)
# arabalar.sort()
# print(arabalar[:])


#.reverse() => dizi içerisindeki elemanları sıralamadan tersine çevirir
print(arabalar[:])
arabalar.reverse()
print(arabalar)

# .len() => dizinin uzunluğunu teslim eder 
print(len(arabalar))

del arabalar # sehirler dizisini tamamen silmiş olursunuz , bu satır derlendikten sonra , alt satırda arabalar dizinine ulaşamayacaksınız
print(arabalar)






