
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

num = random.randint(1,101)
print(x)
guess = 0
hak = 3
point = 100
while hak > 0:
    hak -= 1
    guess = int(input("guess : "))

    if  guess == num:
        print("you know")
        break
    elif num > guess:
        print("yukarı")
    else:
        print("asagı")
if hak == 0:
        print(f"hakkınız bitti tutulan sayı {num}")

        








