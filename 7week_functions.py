# bankamatik uygulaması

sadikHesap = {
    "ad": "Sadık Turan",
    "hesapNo":"123456",
    "bakiye":3000,
    "ekHesap":2000
}

aliHesap = {
    "ad": "Ali kaya",
    "hesapNo":"232652",
    "bakiye":2000,
    "ekHesap":1000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap["ad"]}")

    if hesap["bakiye"] >= miktar:
        print("paranızı alabilirsiniz")
    else:
        toplam = hesap["bakiye"]+hesap["ekHesap"]

        if toplam >=miktar:
            ekHesapKullanimi = input("Ek hesap kulanılsın mı e/h : ")

            if ekHesapKullanimi =="y":
                print("paranızı alınız")
            else:
                print(f"{hesap["hesapNo"]} nolu hesabınızda {hesap["bakiye"]} bulunmaktadır.")


paraCek(sadikHesap,33500)