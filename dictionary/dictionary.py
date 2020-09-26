# dictionary() key value formatında dataları listelemek için kullanılır. JSON formatında data tutar , WebApi(servisler) , Javascript , Angular , React(js-native) gibi birçok platform desteklemekterdir


personeller = [
    {
        "Id" : 1,
        "indexNo" : 0,
        "firstName" : "Tarık",
        "lastName" : "Kotan",
        "mail" : "tarik.kotan@bilgeadam.com",
        "phone" : "+905340886128"
    },
    {
        "Id" : 2,
        "indexNo" : 1,
        "firstName" : "Murat",
        "lastName" : "Vuranok",
        "mail" : "murat.vuranok@bilgeadam.com",
        "phone" : "+905456158234"
    }
]
print(personeller[0])


print(personeller[1]["firstName"])
print(personeller[1]["lastName"])
print(personeller[1]["phone"])

#dictionary içersinde yer alan bir kaydı güncellemek isterseniz

i = 0 # hangi eleman güncellenecek

key = "firstName"
value = "Şahin"

oldRecord = personeller[i][key]

personeller[i][key] = value

newRecord = personeller[i][key]

print(oldRecord)
print(newRecord)

firstname = input("lütfen adınızı giriniz : ")
lastname = input("Soyadınızı giriniz : ")
phone = input("Telefon numaranızı giriniz : ")

id = len(personeller)
indexNo = id - 1

personeller.append({"Id":id,"indexNo":indexNo,"firstName":firstname,"lastName":lastname,"mail":f"{firstname}.{lastname}@bilgeadam.com","phone":phone})

print(personeller[2]["firstName"])

