#index = 0

#while index < 100:
 #   print("index değeri",index)
  #  index = index + 1

# 1 ile 1000 arasında yer alan çift sayıları ekrana yazdırınız

#index = 2
#while index <= 1000:
#   print(index)
  #  index = index + 2

# 1 ile 1000 arasında yer alan tek ve çift sayıların adedini yazın

#index = 1
#teksyilerintoplami = 0
#ciftsayilerintoplami = 0
#while index <= 1000:
#    if index % 2 == 0:
#       ciftsayilerintoplami = ciftsayilerintoplami + 1
#    else:
#        teksyilerintoplami = teksyilerintoplami + 1
#    index = index + 1
#print("tek sayıların toplamı :", teksyilerintoplami, "\nçift syıların toplamı :",ciftsayilerintoplami)




# dışardan girilen metnin her bir elemanını alt alta yazdırınız

#index = 0
#metin = input("lütfen bir metin giriniz :")
#while index < len(metin):
#    print(metin[index])
#    index = index + 1


# dışardan girilen sayıların birbiriyle olan toplam değerini teslim eden uygulama

result = 0
index = 0
sayı = (input("lütfen sayı giriniz :"))
while index < len(sayı):
    result += int(sayı[index])
    index = index + 1
print("sonuc:",result)



