
from isort import file

def not_hesaplama(satir):
    satir = satir[:-1]
    liste = satir.split(":")
    ogrenciAdi = (liste[0])
    notlar = liste[1].split(",")

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (int(not1)+int(not2)+int(not3))/3
    
    if ortalama >= 90 and ortalama <= 100:
        harf ='AA'
    elif ortalama >= 85 and ortalama < 90:
        harf ='BA'
    elif ortalama >= 80 and ortalama < 85:
        harf ='BB'
    elif ortalama >= 75 and ortalama < 80:
        harf ='CB'
    elif ortalama >= 70 and ortalama < 75:
        harf ='CC'
    elif ortalama >= 65 and ortalama < 70:
        harf ='DC'
    elif ortalama >= 60 and ortalama < 65:
        harf ='DD'
    elif ortalama >= 55 and ortalama < 60:
        harf ='FD'
    elif ortalama >= 50 and ortalama < 55:
        harf ='FF'
    elif ortalama >= 0 and ortalama < 50:
        harf ='FF'
    return ogrenciAdi+': ' + harf + '\n'
def ortalamalari_oku():
    with open('sinav_notlari.txt','r',encoding='utf-8') as file:
        for satir in file:
            print(not_hesaplama(satir))
def not_gir():
    ad = input("Öğrenci Adını giriniz: ")
    soyad = input("Öğrenci Soyadını giriniz: ")
    not1 = (input("1. notunuzu giriniz: "))
    not2 = (input("2. notunuzu giriniz: "))
    not3 = (input("3. notunuzu giriniz: "))
    with open("sinav_notlari.txt", "a",encoding="utf-8")  as file:
       file.write(ad+" "+soyad+": "+str(not1)+","+str(not2)+","+str(not3)+"\n")
def not_kayit():
    with open('sinav_notlari.txt','r',encoding='utf-8') as file:
        lise = []
        for i in file:
            lise.append(not_hesaplama(i))
        with open('sonuclar.txt','w',encoding='utf-8') as file2:
            file.writelines(lise)
            for i in lise:
             print(i) 
while True:
    
 islem = input('1- Notları Oku \n2- Not gir \n3- Notları kaydet \n4- Çıkış İşlemi \n')

 if islem == '1':
     ortalamalari_oku()
 elif islem == '2':
     not_gir()
 elif islem == '3':
     not_kayit()
 else:
     break

