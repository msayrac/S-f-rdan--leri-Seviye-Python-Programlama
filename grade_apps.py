
def ortalamalari_oku():
    pass

def not_gir():
    ad = input("Ögrenci Adı :")
    soyad = input("Öğrenci Soyad : ")
    not1 = input("Not 1 : ")
    not2 = input("Not 2 : ")
    not3 = input("Not 3 : ")

    with open("sinav_notlari.txt","a",encoding="utf-8") as file:
        file.write(ad+ " "+ soyad + ":"+ not1+ ", ", not2+ ", "+ not3+"\n")

def notlari_kayitet():
    pass



while True:
    islem = input("1- Notları Oku\n2- Not Gir\n3- Notları Kayıt Et\n4- Çıkış\n")

    if islem == "1":
        ortalamalari_oku()
    elif islem == "2":
        not_gir()
    elif islem == "3":
        notlari_kayitet()
    else:
        break







