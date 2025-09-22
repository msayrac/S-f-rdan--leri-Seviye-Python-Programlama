# # object oriented programing


# # class

# # liste = [1,2,3] # liste list clasından türetilmis

# # result = type(liste)
# # print(result)

# # list1 = [ 1,2,3,4]


# # class

# class Person:

#     # class attributes
#     address = "no information"
    
#     # constructor
#     def __init__(self,name,year):
        
#         # object atttributes
#         self.name = name
#         self.year = year
#         # print("init metodo calıstı")

#     # instance methods
#     def intro(self):
#         print("hello "+ self.name)
    
#     def calculateAge(self):
#         return 2025-self.year
    


# p1 = Person(name = "ali", year = 1980)
# p2 = Person("Veli",2000)

# # update
# p1.name = "Kemal"
# p1.address = "Sivas"
# #accessing object attributes
# print(f"name : {p1.name} year : {p1.year} address : {p1.address}")

# p1.intro()

# p2.intro()


# # print(f"I am {p1.name} and I am {p1.calculateAge()}")

class Circle:
    # class object attribute
    pi = 3.14

    def __init__(self,r=1):
        self.r = r
    
    # methods
    def cevre_hesabi(self):
        return 2*self.pi * self.r
    
    def alan_hesapla(self):
        return self.pi *(self.r)**2
    
c1 = Circle()
c2 = Circle(5)

print(c1.alan_hesapla())
print(c1.cevre_hesabi())


print(c2.alan_hesapla())
print(c2.cevre_hesabi())
