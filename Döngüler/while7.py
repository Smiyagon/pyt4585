sayilar = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

i = 0
tek_sayilar =[]
cift_sayilar= []

while i< len(sayilar):
    if sayilar[i] % 2 == 0:
        cift_sayilar.append(sayilar[i])
    else:
        tek_sayilar.append(sayilar[i])
    i += 1

print(f"Tek sayıların adedi: {len(tek_sayilar)}\nÇift sayıların adedi : {len(cift_sayilar)}")