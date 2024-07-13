#Değişkenlere atanan verilerin veri tipini yazdıran kod.
isim=str("Merhaba")
pisayisi=float(3.14)
sayi=int(110)
x=complex(1j)
y=["apple","banana","cherry"]
z=("apple","banana","cherry")

print("1. Veri tipi : ",type(isim))
print("2. Veri tipi : ",type(pisayisi))
print("3. Veri tipi : ",type(sayi))
print("4. Veri tipi : ",type(x))
print("5. Veri tipi : ",type(y))
print("6. Veri tipi : ",type(z))

#bir sayının pozitif çift sayı olup olmadığını söyleyen program .
sayi=int(input("Bir sayi giriniz :"))
if sayi>0:
    if (sayi%2==0) :
        print("Sayi çift pozitiftir : ",sayi)
        
    else :
       print("Sayi tek pozitif  : ",sayi) 
else :
    if(sayi%2==0):
        print("Sayi çift negatif : ",sayi)
    else:
        print("Sayi tek negatif : ",sayi) 


#Not ortalaması;0-49 arasında ise öğrenciyi bırakan 50-100 arasında ise o dersten geçiren python kodunu yazınız.

x=int(input("Notunuzu Girin :"))

if(x>=0 and x<50):
    print("Dersten Kaldiniz ..")
elif(x>=50 and x<=100):
    print("Dersten Geçtiniz..")
else:
    print("Yanlış Giriş")
#else şart yazılmaz !! "if" değilidir.
#2 ve daha fazla şart varsa "elif" kullan

#Kullanıcı adı ve parola bilgileri ile giriş kontrolü yapan, python kodlamasını yapınız

kadi = 'istinye'
sifre = 'abc123'

gkadi = input('Lütfen kullanıcı adınızı giriniz : ')
gsifre = input('Lütfen şifrenizi giriniz: ')

if(gkadi == kadi and gsifre == sifre):
        print('Giriş başarılı, Blackboard’ı kullanabilirsiniz...')

elif(gkadi == kadi and gsifre != sifre):
        print('Giriş şifreniz yanlış')

elif(gkadi != kadi and gsifre == sifre):
        print('Kullanıcı adınız yanlış')

else:
        print('Giriş bilgileriniz yanlış')

vize1=float(input("1.Vize Notunuzu Girin:"))
vize2=float(input("2.Vize NotunuzuGirin:"))
final=float(input("Final Notunuzu Girin:"))

#Genele Not Ortalaması Hesaplama Programı

GNO=(vize1+vize2)/2*0.4+final*0.6
print("Genel Not Ortalamanız :",GNO)
if(final>=50):
    if(GNO>=50 and GNO<55):
        print("Dersten DD ile Geçtiniz :",GNO)
    elif(GNO>=55 and GNO<60):
        print("Dersten DC ile Geçtiniz :",GNO)
    elif(GNO>=60 and GNO<65):
        print("Dersten CC ile Geçtiniz :",GNO)
    elif(GNO>=65 and GNO<70):
        print("Dersten CB ile Geçtiniz :",GNO)    
    elif(GNO>=70 and GNO<75):
        print("Dersten BB ile Geçtiniz :",GNO)
    elif(GNO>=75 and GNO<85):
        print("Dersten BA ile Geçtiniz :",GNO)
    elif(GNO>=85 and GNO<=100):
        print("Dersten AA ile Geçtiniz :",GNO)
else:
    print("Dersten FF Kaldınız : ",GNO)

#match case kullanımı python 3.10 ve üzeri sürümlerde geçerli !!
sayi = int(input("Bir sayı giriniz :"))
durum=(sayi%2)
match (durum):
    case 0:
        print("Girdiğiniz sayı ÇİFT SAYIDIR")
    case 1:
        print("Girdiğiniz sayı TEK SAYIDIR")

#Güne göre Ders Programını söyleyen program
gun=input("Gün yazın :")
match(gun):
    case "pazartesi":
        print("Veritabanı Sistemlerine Giriş , Sayısal Elektronik , Senaryo Yazarlığı")
    case "salı":
        print("Algoritma ve Programlama")
    case "cuma":
        print("Web Programlama")
    case _:
        print("Bugün Dersin Yok")
#case "cuma or Cuma or CUMA": "KABUL ETMİYOR!!" Bütün bir cümleyi koşul olarak algıladı



        