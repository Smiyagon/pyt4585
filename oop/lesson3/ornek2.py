class BasePhone():
    def __init__(self):
        #Protected
        self._phoneType = "Ahizeli Telefon"
        self.connectionType = None
        self.brand = None
        self.phoneType  = self._phoneType
    def __str__(self):
        return f"Telefonun Türü: {self._phoneType}\nTelefonun Bağlantı Türü: {self.connectionType}\nTelefonun Markası: {self.brand}"

basePhone = BasePhone()
basePhone.connectionType = "Kablolu Bağlantı"
basePhone.brand = "Alcatel"
print(basePhone)
basePhone.phoneType = "Mobil"
print(basePhone.phoneType)

class MobilPhone(BasePhone):
    def __init__(self):
        self.HasCamera = None
        self._phoneType = "Mobil Bağlantı"


mobil = MobilPhone()
mobil.HasCamera = True
mobil.brand = "Nokia"
mobil.connectionType = "Mobil Connection available"

    
class SmartPhone(MobilPhone):
    def __init__(self):
        self.frontCam = None
        self._phoneType = "Smart Phone"


smartPhone = SmartPhone()
smartPhone.brand = "apple"
smartPhone.HasCamera = True
smartPhone.connectionType = "5G"
smartPhone.frontCam = True


