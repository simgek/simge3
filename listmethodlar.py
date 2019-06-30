# .append() dizi içine eleman eklemek için kullanılır
# .append() eklem işlemine dizinin sonundan başlar eklenen her bir eleman dizinin son elemanıdır

sehirler = []

sehirler.append("ankara")
# bu alana insert yapar
sehirler.append("edirne")
sehirler.append("istanbul")
sehirler.append("istanbul")
sehirler.append("izmir")
sehirler.append("malatya")

print(sehirler[:])


# .insert() dizinin içerisinde belirtilen alana ekleme işlemi yapar

sehirler.insert(1,"sivas")
print(sehirler[1])

# 1. paranetre hangi index değperine
# 2. parametre o index değerine hangi eleman eklenecek


# .count() dizi içerisinde yer alan elemanların dizi içerisinde kaç defa geçtiğini teslim eder

print("dizi içerisinde istanbul", sehirler.count("istanbul"),"adet içermektedir")
# dizinin içerisnde istanbul 2 adet içermektedir



# .pop() dizi içerisnde elelman silmek parametre verşlrse erilen index değerindeki elemanı siler parametre verilmez ise dizinin en son elelmanını siler
# .pop() metodunu özelliği silineb elemanı geriye teslim eder

print(sehirler[:])
# print(sehirler.pop(1))
print(sehirler[:])

print(sehirler[:])
print(sehirler.pop())
print(sehirler[:])


# .remove() dizi içerisindeki eleman silme eleman silmek için object olarak nesne ister
# (pop index mantığı ile remove ise, object mantığı ile çalışır)
# index değeri üzerinden eleman silme işlemi gerçekleştirmeez eğer içerde aynı değerne sahip ( 2 adet istanbul gibi)
# eleman var ise soldan sağa doğru bulduğu ilk elemanı silecektir

print(sehirler[:])
print(sehirler.remove("istanbul"))
print(sehirler[:])

# .sort() dizinin elemanlarını a dan z ye > 0 dna 9 a sırlama işlemi yapar

print(sehirler[:])
sehirler.sort()
print(sehirler[:])

# .reverse() dizi içeindeki elemanları tersine çevirir kesinlikle sıralama işlemi yapmaz diziyi olduğu gibi tersine yazar

print(sehirler[:])
sehirler.reverse()
print(sehirler[:])



print(len(sehirler))
print(sehirler[:])

del sehirler # sehirler dizisini tamamen siler artık sonraki kod bloklarında bi elemana ulaşamazsınız

print(len(sehirler))
print(sehirler[:])










