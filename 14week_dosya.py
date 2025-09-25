
# open files open(dosya_adi,dosya_erisme_modu) func kullanırız

# dosya_erisme_modu => dosyayı hangi amacla actigimizi belirtir

# w: write yazma modu

# a apend ekleme

# x create

# r read 

# w

# file = open("newfile.txt","w")

# file.close()


# file = open("C:/Users/lenovo/Desktop/newfile.txt","w")
# file.close()

# file = open("newfile.txt","w",encoding="utf-8")
# # file.write("Sadik Kayaaaa")

# file.close()

# a modu

# file = open("newfile.txt","a",encoding="utf-8")

# # file.write("\nKemal")
# file.write("Deniz\n")
# file.close()


# x create olusturma. Dosya zaten varsa hata verir

# file = open("newfile1.txt","x",encoding="utf-8")

# try:
#     file = open("newfile.txt","r")

#     print(file)
# except Exception as ex:
#     print("dosya okuma hatası", ex)
# finally:
#     print("dosya kapandı")
#     file.close()


# file = open("newfile.txt","r",encoding="utf-8")

# for i in file:
#     print(i,end="")
# file.close()

# content1 = file.read()

# print("icerik 1")
# print(content1)

# file = open("newfile.txt","r",encoding="utf-8")
# content2 = file.read(5)
# content2 = file.read(3)
# content2 = file.read(2)

# print("icerik 2")
# print(content2)

# file.close()

# file = open("newfile.txt","r",encoding="utf-8")

# liste = file.readlines()

# print(liste)

# file = open("newfile.txt","r",encoding="utf-8")

# content = file.read()
# print(content)
# file.close()

# file.close() demeye gerek yok
# with open("newfile.txt","r",encoding="utf-8") as file:
#     content = file.read()
#     print(content)
#     file.seek(10) # cursoru basa gonderir

#     print(file.tell()) # cursor konumunu verir

#     content2 = file.read()
#     print(content2)


# with open("newfile.txt","r+",encoding="utf-8") as file:

#     print(file.read())

# with open("newfile.txt","r+",encoding = "utf-8") as file:
#     file.seek(200)
#     file.write("deneme")

# with open("newfile.txt","r+",encoding="utf-8") as file:

#     print(file.read())

# with open("newfile.txt","a",encoding="utf-8") as file:
#     file.write("\ncan")


# with open("newfile.txt","r",encoding="utf-8") as file:
#     print(file.read())













