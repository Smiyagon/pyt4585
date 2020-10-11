def square(number):
    # result = number**2
    # return result

    return number**2


square = lambda num : num**2 


print(square(4))

my_numbers = [1,2,3,4,5,6,7,8]

# map => döngü mantığı ile dizi içerisindeki her bir eleman üzerinde işlem yapar
retVal = list(map(lambda num: num**2,my_numbers))
for i in retVal : print(i)

# oluşan result içerisinde verilen filtreye göre sonuç kümesinde filtreleme yapar
retBul = list(filter(lambda num: num%2 == 0,my_numbers))
for i in retBul : print(i)

