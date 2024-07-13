x=0
toplam=0
while x<=100:
    x+=1
    if (x%2==0):
        continue
    toplam=toplam+x
print(f"Toplam : {toplam}")

x=0
toplam2=0
while x<=100:
    x+=1
    if (x%2==1):
        continue
    toplam2=toplam2+x
print(f"Toplam : {toplam2}")

toplam3=toplam+toplam2
print(toplam3)

x=1
a=0
b=0
while x<=100:
    if x%2==1:
        print(f'Tek sayı :{x}')
        a=a+x
    else:
        print(f'Çift sayı :{x}')
        b=b+x
    x+=1
print("bitti")
print("Tek sayıların toplamı :",a)
print("Çift sayıların toplamı :",b)


import random
rand=random.randint(1,100)
sayac=0


while True:
    sayac+=1
    sayi=int(input("1 ile 100 arasında değer girin (0 Çıkış) :"))
    if (sayi==0):
        print("Oyunu İptal Ettiniz . ")
        break
    elif sayi<rand:
        print("Daha yüksek bir sayı girin .")
        continue
    elif sayi>rand:
        print("Daha düşük bir sayi girin :")
        continue
    else:
        print("Rastgele seçilen sayı : {0}".format(rand))   # {0} indisi belirler başlangıç için yanına , koyup {1} yazarak yanına ilave yapabilirsin. 
        print("Tahmin sayınız {0}".format(sayac))
        break
    

# for (i=0;i<=100:i++) i 0 ile başlar ; i 100 eşit küçüktür : i 1 artar dmektir diğer programlama dillerinde
for i in range(0,100,1): #python yazılışı "100" dahil değildir UNUTMA !!)
    print(i)

for i in range(0,5,): #OTOMATİK RİTMİK ARTAR ."5" dahil değildir UNUTMA !!)
    print(i)

sayi=int(input("Bir sayı girin :"))
for i in range(2,sayi):
    if sayi%i==0:
        print (f"{sayi} Sayısı Asal Değildir")
        break
else:
    print(f"{sayi} Sayısı Asaldır .")
    

toplam=0
for sayi in range(1,11):
    if sayi%2==0:
        continue
    toplam += sayi
print(f"Tek Sayıların Toplamı : {toplam}")

for sayi in range (5): # 0 dan 5 e kadar olan sayıları yazdırır.
    print (sayi)

for sayi in range (0,-10,-2): # 0 dan -10 a kadar 2 şerli azaltarak NEGATİFLER FARKLI !
    print (sayi)

sayilar = [10,20,30,40,50]
for sayi in sayilar:
    print("Toplam :" , sayi)  #sayılar dizinini sanal bir diziye aktarır ve sayi sanal dizisini yazdırır .

sayilar = [1,2,3,4,5]
toplam=0
for sayi in sayilar:
    toplam += sayi
print("Toplam :" , toplam)  

sehirler=["Ankara","İstanbul","İzmir"]
for sehir in sehirler :
    print(f"{sehir}: {len(sehir)} karakter")
    print(f"{len(sehir)} karakter")  # sehirşerdeki kelimelirin uzunlukrını yazar

kelime="Python"
for harf in kelime:
    print (harf)

kelime="Python"
for harf in reversed(kelime):  #reversed tersten yazdırır
    print (harf)

renkler=("kırmızı","yeşil","sarı","mor")
for renk in renkler:
    print(renk)  # renkleri alt alta yazar 

meyveler=("elma","armt","kraz")
for indeks,meyve in enumerate(meyveler):
    print(f"{indeks}: {meyve}")  #indeksini ve meyveyi eşleştirme
    

ogrenciler= {"1001":"Ahmet","1002":"Ayşe","1003":"Mehmet"}
for ogrenci_no,ogrenci_ad in ogrenciler.items():
    print(f"Öğrenci No : {ogrenci_no} , Öğrenci Adı: {ogrenci_ad}")


for i in range(1,6):
    for j in range(1,6):
        carpim=i*j
        print(f"{i}*{j}={carpim}")


for i in range(1,11):
    for j in range(1,11):
        print("{}x{}={}".format(i,j,i*j))
    print("")


aranan=input("Aranan İsmi girin :")
isim=["ayhan","ayşe","aslı","mehmet","deniz"]
for isimler in isim :
    if isimler == aranan:
        print (f"{aranan} bulundu .")
else:                                  #else for a bağlı değilse olarak çalışıyor .
    print("Bulunamadı")


toplam=0
sayi1=input("1. sayı:")
sayi2=input("1. sayı:")

for i in range(int(sayi1),int(sayi2)+1,1):
    toplam +=i
print("{0} ile {1} arasındaki sayıların toplamı : {2}".format(sayi1,sayi2,toplam))

