class ParentClass():
    def send_message(self,message):
        print("Parent class mesaj servisinehoş geldiniz : ",message)


class BaseClass(ParentClass):
    def send_message(self,message):
        #override var olan bir nesneyi yeniden düzenlemek, aynı isimde, bu sınıf içerisinde tanımlamanız yeterlidir. 
        #eğer miras aldığınız sınıf içerisinden gelen değere de ihtiyacınız varsa super() metodunu kullanarak o değeri elde edersiniz
        super().send_message("Bir önceki sınıfın mesaj metodunu tetikledik")
        print(message)


parent = ParentClass()
parent.send_message("Parent sınıfı içerisindeki mesaj yazdırılmaktadır.")

base = BaseClass()
base.send_message("Base sınıfından gönderilen mesaj")