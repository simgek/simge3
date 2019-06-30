# dictionary key value formatında dataları listelemek için kullanılır json formatında data tutar
# mongodb , webapi (servisler) javascript gibi birçok program bunları desdtekler

personeller = [
    {
        "Id"        :1,
        "Indexno"   :0,
        "Firstname" :"Simge",
        "Lastname"  :"Karademir"
    },
    {
        "Id"        :2,
        "Indexno"   :1,
        "Firstname" :"Okan",
        "Lastname"  :"Muzikacı"
    },
    {
        "Id"        :3,
        "Indexno"   :2,
        "Firstname" :"Rabia",
        "Lastname"  :"Tüylek"
    }
]

# listenin index değerine göre o elemanınekrana yazdırma
print(personeller[0])



# dizi içerisinde eğer bir index değerindei elemanın herhangi bir propertysini ekrana yazdırmak için
print(personeller[0]["Firstname"])
print(personeller[1]["Lastname"])


# liste içerisinde yer alan bir elelmanı güncellemek istşyorsanız
guncellenecekindex = 2
gunvellenecekvalue = "Firstname"
oldname = personeller[guncellenecekindex][gunvellenecekvalue]
personeller[guncellenecekindex][gunvellenecekvalue] = "Murat"
print(oldname,"adlı Personelin adı", personeller[2]["Firstname"],"olarak güncellenmiştir")

personeller.append({"Id":4 , "Index no":3, "Firstname": "Beste", "Lastname":"Karademir"})
print(personeller[:])

print("Personelin Adı :" + personeller[0]["Firstname"] + "\nPersonel soyadı :" + personeller[1]["Lastname"])
print("Personelin Adı :",  personeller[0]["Firstname"], "\nPersonel soyadı :", personeller[1]["Lastname"])
print("Personel Adı : {}\nPersonel Soyadı : {}".format(personeller[0]["Firstname"],personeller[1]["Lastname"]))

