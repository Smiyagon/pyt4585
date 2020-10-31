a = 40 # değeri 40 olan sayısal bir değişken tanımladık

print(type(a)) #<class 'int'>

b = a # b adında bir değişken tanımladık referansını a değişkeninden almasını sağladık.

c = [b] # c değişkeni tanımlayıp b değerini elemanı olarak atadık

print(type(c)) #<class 'list'>

del a  # a değişkennini ram üzerinden sildik.
#print(a) # NameError: name 'a' is not defined

print(b) # 40  => a içerisinde yer alan veriyi b adındaki değişkene kopyaladığınızdan ,ram üzerinde b değişkeni için yeni bir alan oluşmuş olur o yüzden a değerini silsenizde b üzerindeki veriyi tutmaya devam eder
b = 100 # b değişkeninin değerini 100 olarak değiştirdik. 
print(b) #100


class Point:
    def __init__(self,x= 0,y = 0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name,"heap alan üzerinden silindi.")


point1 = Point()
point2 = point1
point3 = point2

print(id(point1),id(point2),id(point3)) # ramdeki adresi ekrana yazdırır.


c = 10 #4362341344  ram üzerindeki adresi
y  = c #4362341344

print(id(c),id(y))

y = 100 #4362344224
print(id(y))


del point1
del point2
del point3