from Employee import Calisan

class Yonetici(Calisan): #yönetici sınıfına çalışan sınıfını miras veriyoruz

    def __init__(self,firstname,lastname,salary,department,age = 18,employeeCount = 0):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.department = department
        self.age = age
        self.employeeCount = int(employeeCount)
    
    def bilgiGoster(self):
        info = super().bilgiGoster()
        return f"{info}{'Yöneticinin Toplam Çalışan Sayısı':40}:{self.employeeCount}\n"
    
    def printBase(self):
        for base in self.__class__.__bases__:
            print("Bu sınıfın miras aldığı sınıf :",base.__name__,"\n")

    def __str__(self):
        info = super().__str__()
        return f"{info} Yöneticidir.\n"
    


yonetici = Yonetici("Ahmet","Şahin",10000,"Yazılım",50,10)
info = yonetici.bilgiGoster()
print(info)
yonetici.printBase()
print(yonetici)

