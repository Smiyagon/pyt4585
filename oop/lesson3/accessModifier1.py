class Cup1:
    """
    docstring
    """
    def __init__(self):
        self.color = None # Public Variable
        self.content = None # Public variable

    def fill(self,beverage):
        self.content = beverage

    def empty(self):
        self.content = None
    
    def __str__(self):
        return self.color  + " " + self.content

cup1 = Cup1()

cup1.color = "Red"
cup1.content = "Tea"

print(cup1) 
cup1.empty()
cup1.content = "coffee"
print(cup1)

class Cup2:
    def __init__(self):
        self.color = None # public variable
        self._content = None # protected variable

    def fill(self,beverage):
        self.content = beverage

    def empty(self):
        self.content = None

    def __str__(self):
        return self.color 

cup2 = Cup2()

cup2.color = "Yellow"
#kullanım şekli yanlıştır
cup2._content = "tea"  # _ ile işaretlenişse korumalıdır değişken tanımlanmamalıdır.
# _ bir alt tire ile işaretli ise , protected anlamına gelir ve bu değere sınıf üzerinden değil miras verilen sınıf üzerinden erişim sağlanır
print(cup2)

class Cup3:
    def __init__(self):
        self._color = None #korumalı variable
        self.__content = None # Gizli variable
    
    def __str__(self):
        return self._color  + " " + self.__content
        

cup3 = Cup3()
cup3._color = "red"
cup3.__content = "tea"

print(cup3.__content)
