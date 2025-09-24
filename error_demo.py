
# liste = ["1","2","5a","10b","abc",10]

# for x in liste:
#     try:
#         result = int(x)
#         print(result, " : sayısal degerdir")
#     except Exception as ex:
#         print(f"{x} : sayısal deger degildir")


# while True:
#     sayi = input("sayi : ")
#     if sayi == "q":
#         break

#     try:
#         result =float(sayi)
#         print("girdiginiz sayi : ", result)
#     except Exception as ex:
#         print( "gecersiz sayi", ex)
#         continue



# def check_password(password):
#     turkce_karakterler = "şçğüöıİ"    

#     for i in password:
#         if i in turkce_karakterler:
#             raise TypeError("Parola tüekçe karkater içeremez")
#         else:
#             pass

#     print("gecerli parola ")

# password = "1555hi"

# try:
#     check_password(password)
# except Exception as ex:
#     print("hata : ",ex)

def factoriyel(x):
    x = int(x)

    if x < 0:
        raise ValueError("Negatif deger")
    
    result = 1

    for i in range(1, x+1):
        result *= i

    return result

for x in [5,10,-10,-3, "10a"]:
    try:
        y = factoriyel(x)
        print(f"{x}! : ", y)
    except Exception as ex:
        print("hata : ", ex)
        continue
