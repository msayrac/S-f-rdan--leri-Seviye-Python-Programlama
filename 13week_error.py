
# # error => hata

# # print(a) # NameError

# # int("12a") # ValueError

# # print(10/0) #ZeroDivisionError

# # print("denem"e) # SyntaxError


# # error handling =>

# # try:
# #     x = 5
# #     y = int(input("y : " ))
# #     print(x/y)
# # except (ZeroDivisionError,SyntaxError,ValueError):
# #     print("sıfır gırılemez")

# # try:
# #     x = 10
# #     y = 0
# #     print(x/y)
# # except Exception as ex:
# #     print("yanlıs bilgi giriniz",ex)
# # else:
# #     print("hersey yolunda")
# # finally:
# #     print("finally blog calıstı")

# # x = 10
# # if x > 5:
# #     raise Exception("x 5 ren buyuk deger alamaz")

# def check_password(psw):
#     import re # regular expression
#     if len(psw) < 8:
#         raise Exception("paralo 8 karakteren buyuk olmalı")
#     elif not re.search("[a-z]",psw):
#         raise Exception("paralo kucuk harf icermelidir")
#     elif not re.search("[A-Z]",psw):
#         raise Exception("parola buyuk harf icermelidir")
#     elif not re.search("[0-9]",psw):
#         raise Exception("parola özel karakter icermelidir")
#     elif not re.search("[_@$]",psw):
#         raise Exception("parola özel karakter icermelidir")
#     elif re.search("\s",psw):
#         raise Exception("parola bosluk icermemelidir")


# check_password("555555555.*@Aad8")

class Person:

    def __init__(self,name,year):
        if len(name) > 5:
            raise Exception("name alanı fazla karakter iceriyor")
        else:
            self.name = name

p= Person("Ali",2022)









