# # method liste icinde önceden tanımlanmıs bir öge.

# list = [ 1,2,3]

# list.append(4)
# print(list) 

# print(type(list))

# mystring = "Hello"
# print(type(mystring))

# print(mystring.upper())

# # functions

# def sayHello(user):
#     print(f"Hello {user}")

# sayHello("Ali")

# def changeName(n):
#     n = "ada"

# name = "yigit"

# changeName(name)

# print(name)

# def change(n):
#     n[0] = "istanbul"

# sehirler = ["ankara","izmir"]

# change(sehirler)

# print(sehirler)

# def yazdir(kelime, adet):
#     print(kelime*adet)

# yazdir("merhaba\n",10)

# def listeyecevir(*params):
#     liste = []

#     for param in params:
#         liste.append(param)
    
#     return liste

# result = listeyecevir(10,20,30,40,"merhaba")

# print(result)


# lambda expression

# def square(num): return num**2

# numbers = [1,3,5,9]
# result = list(map(lambda num: num**2, numbers))
# print(result)

# square = lambda num: num**2

# print(square(3))

# def check_even(num): return num%2 == 0

# numbers = [1,2,3,4,5]
# # result = list(filter(check_even,numbers))

# result = list(filter(lambda num: num%2 ==0,numbers))

# print(result)

x = "global x"

# def function():
#     x = "local x"
#     return x

# print(function())

# print(x)

name="Ali"
def changeName(new_name):
    name = new_name
    print(name)

changeName("Ada")
print(name)










