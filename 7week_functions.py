# method liste icinde önceden tanımlanmıs bir öge.

list = [ 1,2,3]

list.append(4)
print(list) 

print(type(list))

mystring = "Hello"
print(type(mystring))

print(mystring.upper())

# functions

def sayHello(user):
    print(f"Hello {user}")

sayHello("Ali")

def changeName(n):
    n = "ada"

name = "yigit"

changeName(name)

print(name)

def change(n):
    n[0] = "istanbul"

sehirler = ["ankara","izmir"]

change(sehirler)

print(sehirler)




