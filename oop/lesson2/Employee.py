class Calisan:
    
    
    def __init__(self,firstname,lastname,salary,department,age = 18):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.department = department
        self.age = age
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    def bilgiGoster(self):
        print("\n","***Çalışana ait bilgiler ekrana yazdırılıyor...***","\n")
        
        return f"{'Çalışan Adı':40}:{self.firstname}\n{'Çalışan Soyadı':40}:{self.lastname}\n{'Çalışan Yaşı':40}:{self.age}\n{'Çalışan Maaşı':40}:{self.salary}\n{'Çalışan Bölümü':40}:{self.department}\n"
        
    
    def zamYap(self,yapilanZam):
        print("Çalışanın Maaşına zam yapıldı...","\n")
        maas = self.salary
        self.salary += yapilanZam
        print(f"{self} adlı personelin {maas} olan maaşı {self.salary} olarak düzenlendi.","\n")
    
    def departmanDegis(self,yeniDepartman):
        print("Personelin departmanı değiştiriliyor...","\n")
        departman = self.department
        self.department = yeniDepartman
        print(f"{self} adlı personelin {departman} olan bölümü {self.department} olarak değiştirildi.","\n")


# calisan =  Calisan("Tarık","Kotan",1000,"Yazılım",22)
# calisan.bilgiGoster()
# calisan.departmanDegis("Eleman")
# calisan.zamYap(10000)

