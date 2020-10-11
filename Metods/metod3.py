def Metod(ad,soyad,mail,gorev,*telefon):
    print(f"""
    Personelin Adı         :{ad}
    Personlin Soyadı       :{soyad}
    Personelin Mail Adresi :{mail}
    Personelin Görevi      :{gorev}
    Personelin telefonları :{"-".join(telefon)}
    """)

Metod("tarık","kotan","tarik.kotan","danışman","230315640","405132153301")

