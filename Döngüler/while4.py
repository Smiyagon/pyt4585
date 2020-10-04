# 1 ile 1000 (dahil) arasındaki tek ile çift sayıların toplam adedini ekranı yazdırınız
tek_sayilar= []
cift_sayilar = []
i = 1
while i <= 1000:
    if i % 2 == 0:
        cift_sayilar.append(i)
    else:
        tek_sayilar.append(i)
    i = i+1
        

print(f"Tek sayılar : {len(tek_sayilar)}")
print(f"Çift sayılar : {len(cift_sayilar)}")