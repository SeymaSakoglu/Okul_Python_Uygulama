try:
    a = input("Bir sayı giriniz =")
    a = float(a)
    b=12/a
    print(b)
except:
    print("Hatalı Giriş Yaptınız !")
else:
    print("İşlem Başarılı Gerçekleştirildi .")

##
kontrol = True
try:
    a = input("Bir sayı giriniz =");
    a = float(a);
    b=24/a;
    print(b);
except:
    print("Hatalı Giriş Yaptınız !");
else:
    print("İşlem Başarılı Gerçekleştirildi .");
    kontrol = False
finally:
    if kontrol:
        a = input("Bir sayı giriniz =");
        a = float(a);
        b=24/a;
        print(b);       
    kontrol = False # Programı durdurur . olmasa olur ama koyulursa program orada biter devam etmez !!

##
    
    kontrol = True
try:
    a = int(input("Bir Sayı Giriniz = "))
    b = 12 / a
    print ("b = ",b)
    # kontrol = False # program burada biter
except:
    a = 0.1  
    b = 12 / a
    print ("b = ",b)
    print ("Veri Girişi Başarısız, a ' ya öntanım değeri verildi !")
    # kontrol = False # Olursa program durur Kaldırılırsa
else:
    print ("İşlem Başarı ile Gerçekleştirildi !")
    kontrol = False # Denilirse finally e zıplamaz
finally:
    if kontrol:
        a = int(input("Bir Sayı Giriniz = "))
        b = 12 / a
        print ("b = ",b)

##
        
kontrol = True
try:
    a = int(input("Bir Sayı Giriniz = "))
    b = 12 / a

#except Exception as e:
except ValueError as e:
    print("Veri Girişi Başarısız!...")
    print("Hata Nedeni : ", e)

else:
    print ("İşlem Başarı ile Gerçekleştirildi !")
    print("Girilen değerin 12'ye bölümü :",b )
    kontrol = False
finally:
    if kontrol:
        a = 0.1  
        b = 12 / a
        print("")
        print ("b = ",b)
        print ("Veri Girişi Başarısız, a ' ya öntanım değeri verildi !")

##
# FONKSİYONLAR 

def hello():
    print("Merhaba")

hello()  # Ekrana Merhaba yazar

def fonk(isim):
    print("Merhaba,",isim)

fonk("Şeyma")

#

def fonk(isim):
    print("Merhaba,",isim)

a= input("İsminizi girin :")
fonk(a)

#

def toplama(a,b):
    return a+b
# input öncesi int değeri girilirse sonradan hata çıkmaz . 
a= int(input("Bir sayı girin :"))
b= int(input("Bir sayı daha girin :"))

sonuc =toplama(a,b)

print("Sayıların Toplamı :", sonuc)

##

def toplama(a,b):
    return a+b

giris=input("fonksiyon için 1 çıkış için 0 girin :")

if(giris=="1"):
    a= int(input("Bir sayı girin :"))
    b= int(input("Bir sayı daha girin :"))
    
    print("Sayıların Toplamı :",toplama(a,b))

else:
    exit()

##

def ikisayitopla_test():
    
    s1=int(input("Bir sayı giriniz:"))

    s2=int(input("Bir sayı giriniz:"))

    sonuc=(s1+s2)
    
    print("Sayıların toplamı : ", sonuc)
    
ikisayitopla_test()

##

def emekli(dyil,im):
    yas = 2024-dyil
    emeklilik = 65 - yas
    if emeklilik > 0:
        print(f'{im} emekliliğinize {emeklilik} yıl kaldı')
    else:
        print('Zaten emekli oldunuz')

emek=int(input("Doğum yılınızı giriniz:"));
im=input("İsminizi giriniz :");
emekli(emek,im)

##
# Örnek: Girilen bir sayının tek mi çift mi olduğunu bulan program

def tekcift():
    
    sayi=int(input("Bir sayı giriniz:"))

    if (sayi%2==0):
    
        print(sayi,"sayısı çifttir")

    else:
    
        print(sayi,"sayısı tektir")
giris= input("Fonksiyon için 1 çıkış için 0 girin :")

tekcift()

##
#Örnek: Girilen iki sayı arasındaki asal sayıları bulan program

def asalsayi(sayi1, sayi2):
    for sayi in range(sayi1, sayi2+1):
        if sayi > 1:
            for i in range(2, sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)

sayi1 = int(input('sayı 1:'))
sayi2 = int(input('sayı 2:'))

asalsayi(sayi1, sayi2)

#
# Örnek : Girilen sayıya kadar kendisini tam bölen sayıları bulma

def tambolen(sayi):
    tbdizi = [ ]
    #for i in range(1,sayi+1):    # burada 1 den başlar ve sayının kendisini de dahil eder .
    for i in range(2, sayi):
        if (sayi % i == 0):
            tbdizi.append(i)   # diziye ekleme yapar .append
    return tbdizi

sayi=int(input("Sayıyı giriniz : "))
print(tambolen(sayi))

#
def fibon(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibon(n-1)+fibon(n-2)

for i in range(1,20):
    print(fibon(i), end=" ") # end=" " döngü her bittiğinde boşlık bırakıp yanından devam eder . 

print()

# end"-" ile sep"-" arsındaki farka bakarsın :)

