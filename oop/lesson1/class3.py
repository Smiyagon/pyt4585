class Student:
    """
    self : sınıf içerisinde yer alab metotların diğerlerinden farkı hangi sınıf içerisinde çalıştığını belirtmesidir
    self anahtar kelimesini vererek metodun bu sınıf içerisinde çalıştığını belirtmiş oluruz. 
    Tanımlama yapılırken eklenir fakat kullanım sırasında python bunu bizim için kendisi yapacaktır. 
    """

    FirstName = ""

    def GiveNot(self,student_not):
        print(student, "Adlı Öğrenciye not girişi yapıldı")

    def GivePunish(self,student):
        print(student, "Adlı Öğrenciye ceza verildi")

    def Check(self,student):
        print(student, "Adlı Öğrencinin yoklaması girildi")


student = Student()

student.FirstName = "Tarık"