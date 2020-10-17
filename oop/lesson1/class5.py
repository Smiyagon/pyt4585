import os
from datetime import datetime
from datetime import timedelta


class Employee:
    
    FirstName = ""
    LastName = ""
    Mail = ""
    Phone = ""
    HireDate = f"{datetime.now().day}/{datetime.now().month}/{datetime.now().year} {datetime.now().hour}:{datetime.now().minute}" #sistem tarafından otoamtik eklenecek
    Address = ""
    FireDays = 0
    
    
    def IseAl(self):
        fireDate  = 0
        if(self.FireDays > 0):
            time = (datetime.now()+timedelta(days = self.FireDays))
            fireDate = f"{time.day}/{time.month}/{time.year} {time.hour}:{time.minute}"
        else:
            fireDate = "Gün sayısı belirtilmediğinden, çıkış tairihi hesaplanamadı."
        os.system('clear')
        print("-"*50)
        print(f"{'Personelin adı':40}:{self.FirstName}\n{'Personelin Soyadı':40}:{self.LastName}\n{'Personelin Mail Adresi':40}:{self.Mail}\n{'Personelin Telefonu':40}:{self.Phone}\n{'Personelin Adresi':40}:{self.Address}\n{'Personelin İşe Giriş Tarihi':40}:{self.HireDate}\n{'Personelin sözleşme bitiş tarihi':40}:{fireDate}\nPersonelin girişi yapıldı")
        print("-"*50)
    def Update(self):
        #db içerisinden personeli güncelle
        pass

    def Fire(self):
        #personelin db içerisindeki durumunun değiştirilmesi
        # 1 = aktif , 2 = Pasit , 3 = Delete , 4 = Kovuldu , 5= İşten çıkarıldı 
        pass

personel = Employee()
personel.FirstName = "Tarık"
personel.LastName = "Kotan"
personel.Mail = "tarık.kotan@gmail.com"
personel.Phone = "05340886128"
personel.Address = "İstanbul"
personel.FireDays = 150
personel.IseAl()


