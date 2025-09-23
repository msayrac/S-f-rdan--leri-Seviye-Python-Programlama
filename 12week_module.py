# # uygulamaları parcalara ayırmaya module deriz

# # her bir farklı parcaya farklı gorev veririz

# # birbirleri arasında alısveri yapabilirler

# # main.py modulunde bu islemleri yapabiliriz

# # math modulu

# import math

# # value = dir(math)
# # value_help = help(math)
# # print(value)
# # print(value_help)

# # print(help(math.factorial))

# print(math.sqrt(9))

# import math as islem

# print(islem.factorial(5))

# from math import * # bu durumda module ismini kullanmaya gerke yok

# print(factorial(4))

# from math import factorial, sqrt,ceil

# print(factorial(2))

# import random
# print(random.randint(1,5))

from random import *
print(randint(1,5))

# print(help(random))

# print(random()) #0.0 ile 1 arası sayı

# print(int(uniform(10,100)))

# print(randint(1,10))

# names = ["ali","yagmur","deniz","cenk"]
# result = names[randint(0,len(names)-1)]
# print(result)

# liste = list(range(10))
# shuffle(liste)
# print(liste)

liste = range(10)
print(liste)

result = sample(liste,3)
print(result)

names = ["ali","yagmur","deniz","cenk"]
result = sample(names,2)
print(result)



















