import os
class Clear:
    def clearScreen(self):
        os.system(self)
        print("Ekran temizlendi")
    def ClearStirng(self):
        arg = self.lower().replace(" ","").replace("ş","s")
        return arg


class MathLibrary:
    def toplam(self,*arg):
        toplam = 0
        for i in arg:
            toplam += i
        return toplam

    def fark(self,*arg):
        toplam = 0
        for i in arg:
            toplam -= i
        return toplam
