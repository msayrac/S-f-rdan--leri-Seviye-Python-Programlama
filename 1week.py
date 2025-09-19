
fruits = {"orange","apple","banana"}

# print(fruits[0]) # 'set' object is not subscriptable

for x in fruits:
    print(x)

fruits.add("melon")
fruits.update(["mango","grape","apple"])

print(fruits)

fruits.remove("mango")
fruits.discard("apple")
print(fruits)

fruits.pop()

fruits.clear()

# value types string numbers

x = 5

y = 25

x = y

y = 10

print(x,y)

# reference type => list

a = ["apple","banana"]
b = ["apple","banana"]

a = b

b[0] = "grape"

print(b)
print(a)
