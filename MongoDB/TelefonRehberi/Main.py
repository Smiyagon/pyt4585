from Person import Person
from PersonService import *
import os

def Create():
    per = Person()
    per.FirstName = input("Lütfen kişinin adını giriniz: ")
    per.LastName = input("Lütfen kişinin soyadını giriniz: ")
    per.Phone = input("Lütfen kişinin telefon numarasını giriniz: ")
    per.Mail = input("Lütfen kişinin mail adresini giriniz: ")
    return per
# PersonService.Add(per)

def Start():
    key = "y"
    while key != "e":
        print("Lütfen işlem seçiniz!\nKayıt Ekleme : a\nKişi silmek için : d\nKişileri listeleme : l\nKişileri Güncellemek : u\nÇıkış Yapmak : e")
        key = input("İşlem : ").lower()

        if key == "a":
            person = Create()
            Add(person)
            os.system("clear")
            print("Kayıt başarıyla eklendi.")
        elif key == "d":
            print("Lütfen _id değerini giriniz!")
            id = input("_id : ")
            Delete(id)
            print("Kayıt başarıyla silindi.")
        elif key == "l":
            os.system("clear")
            Show()
        elif key == "u":
            print("Lütfen _id değerini giriniz: ")
            id = input("_id : ")
            Update("")
        elif key == "e":
            print("Çıkış Yapıldı.")
            exit

Start()