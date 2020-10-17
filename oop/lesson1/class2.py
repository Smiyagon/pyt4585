class Employee:
    """
    Personel Sınıfı Oluşturuyoruz
    """
    FirstName  = ""
    LastName   = ""
    Phone      = ""
    Mail       = ""

    
emp = Employee()
emp.FirstName = "Tarık"
emp.LastName = "Kotan"
emp.Phone = "05340886128"
emp.Mail = "tarik.kotan@hotmail.com"

print(emp.FirstName)
