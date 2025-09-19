# # assignment operators

# x = 5
# y = 10
# print(x,y)

# x, y = 50, 100

# print(x,y)

# x, y = y, x
# print(x,y)

# print(11//5)

# # comparison operators

# # username, password => database

# a, b, c, d = 5, 5, 4, 10

# result = a==b
# print(result)

# print(a==c)

# password = "1234"
# username = "sadik"

# print("ssdds"==password)

# # applicaiton

# # a = int(input("a : "))
# # b = int(input("b : "))

# # result = (a>b)

# # print(f"a : {a} b: {b} den büyüktür: {result}")

# # logical operators

# x = 6

# # 5 < x <10

# result = 5 < x <10
# print(result)

# # and or not 

# x = 6

# result = (x > 5 and x < 10)
# print(result)

# x = 5
# result = (x > 5 or x < 10)
# print(result)

# x = 5

# print(x > 0 and x % 2 !=0)

# print(x > 0 and x % 2 == 0)

# print(x > 0 or x % 2 == 0)

# # not tam tersimi alır

# print( 5 > 2)

# print(not(5 > 2))

# mini app

# a = 333

# if a>0 and a <=100:
#     print(f"{a} :  0 ile 100 arasındadır.")
# else:
#     print(f"{a} :  0 ile 100 arasında değildir.")


# Identity operator : is

x = y = [1,2,3]
z = [1,2,3]

print(x == y)
print(x == z)

print(x is y) # aynı reference sahip mi True gelir
print(x is z) # aynı reference sahip değil

x = [1,2,3]
y = [1,2]

print(x is y)

print(x is not y)

#Membership Operator: in

x = ["apple","banana"]

print("banana" in x)

name = "çınar"
print("a" in name)
print("a" not in name)











