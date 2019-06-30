# tanımlama şekli
# bir dizinin max index değeri eleman sayısının bir eksiğidir

sehirler = ["ankara","edirne","istanbul","kayseri","eskişehir","kars","istanbul"]

          # eleman sıra no : 1,2,3
          # eleman index no: 0,1,2

print(sehirler[0])
index = len(sehirler) -1
print(sehirler[index])

print(sehirler[0:4]) # 1.parametrede verilen değer index değeridir 2. parametrede verilen index değerinin bir altdeğerine kadar olan bölüm yazdırır

# dizinin tüm elelmanlarını ekrnan yazdırmak için
print(sehirler[:])