import os
def decorator_metot(func):
    def sarmal_metot():
        os.system("Clear")
    #     print(f"Sarmal Metodu : {metot.__name__}'dan önce tetiklendi")
        return func()
    return sarmal_metot

@decorator_metot
def print_metot():
    print("print_metot tetiklendi.")


print_metot()