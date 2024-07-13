a=1
while a<=10:
    a+=1 
    print("İstinye Üniversitesi")


toplam=0
i=1
while i<=100:
    toplam=toplam+i
    print (i,".","Döngü Toplam =",toplam)
    i=i+1
print  ("Sayıların toplamı =",toplam)


sayi=0
while (sayi<10):
    print("No :",sayi)
    sayi+=1
print ("Güle Güle :)")

while True:
    soru=input("Yapmak istediğin işlemi yaz..Çıkmak için q bas =")
    if soru=="q" or soru=="Q" :
        print ("Programdan Çıkılıyor ..")
        break

while True:
    sayi=input("Bir sayı girin : ")
    if sayi=="23":
        print ("sistemden çıkılıyor...")
        break

a=0
while True:
    print(a)
    a=a+1
    if a>10:
        break

a=0
while True:
    a=a+1
    if a%2==1:
        continue #eğer Sonuç tek sayı olursa işlem yapma ! çift sayı olursa alt satıra geç 20 den büyük olana kadar döngü devam eder
    elif a>20:
        break
    else :
        print(a) #Çift sayıları yazar 

yazi="İstinye Üniversitesi"
es=len(yazi)-1
print(yazi,"Toplamda :",es,"sayı vardır .")

yazi=[0,1,2,3,4,5,6,7,8,9]
es=len(yazi)
print("Toplamda :",es,"sayı vardır")


#Çalışmadı ...
sayi=[0,1,2,3,4,6,7,8,9]  #Diziler 0 ile başlar !!
b=len(sayi)
a= -1
while (a < b):
    a += 1
    print(sayi[a])

sayi=[0,1,2,3,4,5,6,7,8,9]
b=len(sayi)-1 # eleman sayısı 10 -1 yapınca liste dizini içinde kalıyor hata gidiyor -1 i silince sonuç aynı ancak hata da veriyro .İstersen dene :)
a=-1
while a<b:
    a+=1
    print(sayi[a])

    
#Çalıştı
isim=input("Adınızı yazın :")
sayac=0
while sayac<len(isim):
    print(isim[sayac])
    sayac+=1
print("Adının harflerini Listeledim.")


# random 0.0-1.0 arasında sayı üretir . Onu .10 ile çarparsak 0.8.10=8 olur :)
# randomda sayı üretebilmek için "import random" modülünü import etmek gerekir .

import random 
print (random .randint(1,100))  #randint =int bir random sayı üret . int dediğin zaman çalışmıyor


fiyat=50
etiket="Fiyatı {} Tl'dir"    # {arasında boşluk bırakma}
print(etiket.format(fiyat))  # .format(değişken) değişken ifadesini {içine atar}



