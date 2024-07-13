#Girilen Ondalık Değerleri Toplayan Kod
sayi1=float(input("bir sayı giriniz :"))
sayi2=float(input("bir sayı giriniz :"))
top=sayi1+sayi2
print(sayi1," + ",sayi2,"=",top)

# Not Ortalamasını Hesaplayan Kod
vize=float(input("Vize Notunu Girin :"))
proje=float(input("Proje Notunu Girin :"))
final=float(input("Final Notunu Girin :"))
ort=vize*0.3+proje*0.2+final*0.5
print("Ortalama : ", ort)

#Dikdörtgen Alan-Çevre Hesabı Yapan Kod
a=float(input("Dikdörtgenin Uzun Kenarını Girin :"))
b=float(input("Dikdörtgenin Kısa Kenarını Girin :"))
cevre=2*(a+b)
alan=a*b
print("Dikdörtgenin Alanı : ",alan)
print("Dikdörgenin Çevresi : ",cevre)

#Çember Yarıçap Hesabı Yapan Kod
r=float(input("Cemberin Yarı Capını Girin :"))
pi=3.14
alan=pi*r*r
cevre=2*pi*r
print("Alan :",alan)
print("Çevre :",cevre)

#Girilen Sayının Pozitif/Negatif Olduğunu Yazan Kod
a=int(input("Bir sayı girin :"))
if a>0:
    print("Sayı pozitif ")
elif a==0:                # Eğer birden çok ihtimal varsa "elif" bir yada daha çok kullanılabilir :)
    print("Sayı Sıfır")
else:
    print("Sayı negatif ")

# Ehliyet yaşı sorgusu.
isim=input("İsminiz :")
yas=int(input("Yaşınız :"))
egitim=input("Eğitim Durumunuz (Mezun Lise/Üniversite) :")
if (yas >=18):
    if (egitim=="Lise" or egitim=="Üniversite") :
        print(isim,"Ehliyet'e Başvurabilirsin :)")
    else :
        print(isim,"Ehliyete Başvuru Yapamazsın :(")
else :
    print(isim,"Yaşın Tutmuyor :((")

# 4 işlem yapan kod
print("1=Toplama")
print("2=Çıkarma")
print("3=Çarpma")
print("4=Bölme")
a=int(input("Bir sayı girin :"))
b=int(input("Bir sayı girin :"))
c=int(input("İşlemi seçin..."))
if (c==1):
    sonuc=a+b
    print(a,"+",b,"=",sonuc)
elif (c==2):
    sonuc=a-b
    print(a,"-",b,"=",sonuc)
elif (c==3):
    sonuc=a*b
    print(a,"x",b,"=",sonuc)
elif (c==4):
    sonuc=a/b
    print(a,"/",b,"=",sonuc)
else :
    print("Hatalı Giriş Yaptınız")

# Değişkenler "float" olursa ortalama ondalıklı çıkarsa hata vermez
vize1=float(input("1.Vize Notunu Girin :"))
vize2=float(input("2. vize notunu Girin :"))
final=float(input("Final Notunu Girin :"))
ort=(vize1+vize2)/2*0.4+final*0.6
if (ort>=55):
    print("Notunuz :",ort," Dersi geçtiniz ")
else:
    ("Notunuz :",ort," Dersten kaldınız")
    