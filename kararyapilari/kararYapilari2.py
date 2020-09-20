
 try:
    _not = int(input("Lütfen notunuzu giriniz: "))
    
    if (_not >= 0 ) and (_not <= 100):
         print(_not)
    elif _not > 100:
         print("100 den büyük not giremezsiniz")
    else:
        print("0 dan küçük not giremezsiniz")
except:
    print("Sadece not gir!!!")

