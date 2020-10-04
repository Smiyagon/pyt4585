#yaptığımız işlemin sonunda oluşan değeri geriye teslim almak istiyor isek function kullanmalıyız:

# dışarıdan aldığınız 2 sayının toplamını geriye teslim eden metod
def hesapla(x,y):
    toplam = x + y
    return toplam  # returnden sonra bir not bloğu çalışmaz


sonuc = hesapla(9,5)
print(sonuc)
