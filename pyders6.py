#dosya=open("deneme.txt","tx")

#dosya=open("/Users/sakog/OneDrive/Belgeler/OKUL/pyders/vadi.png","br")
# \\ yada / kullanılır
#dosya=open("C:\\Users\\sakog\\OneDrive\\Belgeler\\OKUL\\pyders\\vadi.png","br")
#print(dosya)

#dosya=open("deneme1.txt","w",encoding="utf-8")

dosya=open("deneme.txt","a",encoding="utf-8")
#dosya.write("İstinye Üniversitesi-Bilgisayar Programcılığı Bölümü")
dosya.write("\n'w' komutu eskisinin üzerine yazar")
#dosya.write("'a' komutu yaznın devamına yazar")
dosya.close()  # Bir Dosya Mutlaka Kapatılmalı
# \n komutu alt satıra geçer
dosya=open("deneme.txt","r",encoding="utf-8")
oku=dosya.read()
print(oku)
dosya.close()
#
veri=input("İsminizi Girin :")

dosya=open("deneme.txt","a",encoding="utf-8")
dosya.write("\n"+veri)
dosya.close()  # Bir Dosya Mutlaka Kapatılmalı

dosya=open("deneme.txt","r",encoding="utf-8")
oku=dosya.read()
print(oku)
dosya.close()

#

adi=input("isminizi girin :")
sadi=input("Soyisminizi girin :")
yas=input("yaşınızı girin : ")
dyer=input("doğum yerini girin :")

dosya=open("deneme2.txt","a",encoding="utf-8")
dosya.write("Adı : "+adi+"\n")
dosya.write("Soyadı : "+sadi+"\n")
dosya.write("Yaşı : "+yas+"\n")
dosya.write("Doğum Yeri : "+dyer+"\n")
dosya.close

dosya=open("deneme2.txt","r",encoding="utf-8")
oku=dosya.read()
print(oku)
dosya.close

#

tckim=["56789309221","78965490885","67309832114","738398022113"]
adi=["Aslı","Hülya","Mehmet","Derya"]
soy=["Kara","Uzun","Demir","Sert"]
em=["aslikara@gmail.com","hulyauzun@msn.com","mehmetdemir@yahoo.com","deryasert@msn.com"]
tel=["53478909778","5326578930","5436758234","5543278390"]
hobi=["Voleybol-Treking","Tenis","Yüzme","Futbol"]
dy=["İstanbul","Artvin","Aydın","Denizli"]

dosya=open("deneme1.txt","w",encoding="utf-8")
for i in range(len(adi)):
    dosya.write(tckim[i]+"\n")
    dosya.write(adi[i]+"\n")
    dosya.write(soy[i]+"\n")
    dosya.write(em[i]+"\n")
    dosya.write(tel[i]+"\n")
    dosya.write(hobi[i]+"\n")
    dosya.write(dy[i]+"\n")

dosya=open("deneme1.txt","r",encoding="utf-8")
oku=dosya.read()
print(oku)
dosya.close

#


