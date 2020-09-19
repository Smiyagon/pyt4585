try:
    #db connection open
    sayi = int(input("Lütfen sayı giriniz : "))
    #connection error
    print("Tebrikler bro!")
except :
    print("Vazgeçtim")
finally:
    print("her durumda bir defa tetiklenir.")
    # db connection close
    # En son olarak işlem yapılsa da yapılmasa da bu işlem uygulanması gerekiyorsa finally bölümünün altına yazılması gerekiyor.