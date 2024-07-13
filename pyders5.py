dizi=("Aslı","Sevda","Mehmet","Feyyaz")
a=0
while a<=3:

    print(dizi[a])
    a+=1

dizi=("Aslı","Sevda","Mehmet","Feyyaz")
a=-1
while a<=2:
    a+=1
    print(dizi[a])

liste=["elma","armut","portakal"]
print(liste)
liste.append("Kiraz")  #List sıralıdır eleman ekler / <Tuple> sıralıdır ama eleman eklenmez!!
print (liste)

liste={"elma","armut","portakal"}
print(liste)
liste.add("Kiraz")  # Set eleman ekler ama sırasızdır .oyüzden sona koymak zorunda değil .
print (liste)

ogrenci={"numara" : "120" , "ad":"Ahmet" , "soyad":"Yılmaz"}
print(ogrenci)
ogrenci["cinsiyet"]="E"
print(ogrenci)
print(ogrenci["ad"])   #Sırasız , elamanları değştirilebilir ve indexlenmiş bir dizidir . Tekrarlanmaz

sayılar=[1,2,3,4,5]
kareler=[]

for i in sayılar:         # "i" "sayılar" dizisinden eleman çeker ve "sanal dizi" olur .
    kareler.append(i*i)
print(kareler)

liste=["elma","armut","portakal"]
print(liste)
liste.clear()         # clear() listedeki tüm elemanları siler
print(liste)

dersler=["VTYS","İSTİNYE","ÜNİVERSİTE"]
dersler2=dersler.copy()
print(dersler)
print(dersler2)

dersler=["VTYS","İSTİNYE","ÜNİVERSİTE","İSTİNYE","ÜNİVERSİTE","İSTİNYE","ÜNİVERSİTE","VTYS","İSTİNYE"]
print(dersler.count("İSTİNYE"))
print(dersler.count("VTYS"))
print(dersler.count("ÜNİVERSİTE"))

isimler=["ali","veli","ayşe"]
kisiler=["hasan","mehmet","hayati"]
isimler.extend(kisiler)
print(isimler)   #  Eklenilen liste
print(kisiler)   #  Eklenen liste
kisiler.extend(isimler)
print(isimler)   #Yeni eklentili hali
print(kisiler)   

isimler=["ali","veli","ayşe"]
kisiler=["hasan","mehmet","hayati"]
print(isimler.index("ali"))
print(kisiler.index("mehmet"))

isimler=["ali","veli","ayşe"]
kisiler=["hasan","mehmet","hayati"]
print(isimler)
print(isimler.index("veli"))  # index 1
isimler.insert(1,"hasan")     # listeye 1. index e "hasan " atandı ve "veli" nin sırası kaydı
print(isimler)
print(isimler.index("veli"))  # index 2

liste=["elma","armut","üzüm","limon","karpuz","kavun"]
print(liste)
liste.pop(0)    # verilen indeksi siler
print(liste)
liste.pop()     # veri yoksa sondaki elemanı siler
print(liste)

liste=["elma","armut","üzüm","limon","karpuz","kavun"]
print(liste)
liste.remove("üzüm")    # seçilen elemanı siler
print(liste)
liste.remove("elma")
print(liste)

liste=["elma","armut","üzüm","limon","karpuz","kavun"]
print(liste)
liste.reverse()      # Diziyi tersten yazar
print(liste)

isimler=["ali","veli","ayşe","hasan","mehmet","hayati"]
print(isimler)
isimler.sort()  # alfabetik sıralamaya göre sıralar
print(isimler)

