
# # # # # # def greeting(name):
# # # # # #     print("Hello ", name)

# # # # # # sayHello = greeting

# # # # # # print(sayHello("ali"))
# # # # # # print(greeting("ali"))

# # # # # def outer(num1):
# # # # #     print("outer")
# # # # #     def inner_increment(num1):
# # # # #         print("inner")
# # # # #         return num1 + 1
# # # # #     num2 = inner_increment(num1)
# # # # #     print(num1, num2)
    

# # # # # outer(10)

# # # # def factorial(number):

# # # #     if not isinstance(number, int):
# # # #         raise TypeError("Number must be integer")
# # # #     if not number >=0:
# # # #         raise ValueError("Number must be zero or positive")

# # # #     def inner_factorial(number):
# # # #         if number <=1:
# # # #             return 1
    
# # # #         return number * inner_factorial(number-1)
# # # #     return inner_factorial(number)

# # # # print(factorial(5))


# # # def usalma(number):

# # #     def inner(power):
# # #         return number ** power
    
# # #     return inner

# # # two = usalma(2)

# # def yetki_sorgula(page):

# #     def inner(role):
# #         if role == "Admin":
# #             return "{0} rolunün {1} sayfasına ulaşabilir.".format(role,page)
# #         else:
# #             return "{0} rolunün {1} sayfasına ulaşamaz.".format(role,page)
# #     return inner


# # user1 = yetki_sorgula("Product Edit")

# # print(user1("Admin"))


# def toplama(a,b):
#     return a+b

# def cikarma(a,b):
#     return a-b
# def carpma(a,b):
#     return a*b
# def bolme(a,b):
#     return a/b

# def islem(f1,f2,f3,f4, islem_adi):
#     if islem_adi =="toplama":
#         print(f1(2,3))
#     elif islem_adi == "cikarma":
#         print(f2(5,3))
#     elif islem_adi == "carpma":
#         print(f3(3,4))
#     elif islem_adi == "bolme":
#         print(f4(10,2))
#     else:
#         print("basarısız islem...")

# islem(toplama,cikarma,carpma,bolme,"toplama")

def my_decorator(func):
    def wrapper():
        print("fonksiyondan önce islemler")
        func()
        print("fonksiyondan sonraki islemler")
    return wrapper

@my_decorator
def sayhello():
    print("hello")

@my_decorator
def sayGreeting():
    print("greeting")


sayhello()

sayGreeting()





