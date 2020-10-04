from random import randint



kolon = int(input("Kaç adet kolon oynamak istiyorsunuz : "))
z = 0

while z < kolon :
    sayilar = []
    i = 0
    while i < 6 :
        sayi = randint(1,49) 
        if sayi in sayilar:
            continue
        else:
            nmr = str(sayi)
            if(len(nmr)==1):
                sayilar.append("0"+str(sayi))
            else:
                sayilar.append(str(sayi))
        i+=1    
    sayilar.sort()
    print(f"{i+1}. kolon =","-".join(sayilar))
    sayilar.clear()
        
    z += 1


    
    
       
    




    



