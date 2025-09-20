
# for item in range(2,10,2):
#     print(item)

# print(list(range(5,50,5)))

# enumerate
# index = 0
greeting =  "Hello There"

# for letter in greeting:
#     print(f"index: {index} letter: {greeting[index]}")
#     index += 1

# for index, item in enumerate(greeting):
#     print(index,item)

# zip

# l1 = [1,2,3,4,5]
# l2 = ["a","b","c","d","e"]

# l3 = list(zip(l1,l2))

# print(l3[0][1])

# comprehensions

# for x in range(10):
#     print(x)

# numbers = [x for x in range(0,10,2)]
# print(numbers)

import random 

x = random.randint(1,101)
print(x)
guess = 0
hak = 3
point = 100
while guess != x:
    while hak < 1:
        if hak == 0:
            break
        guess = int(input("guess : "))
        hak-=1








