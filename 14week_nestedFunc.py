
# # def greeting(name):
# #     print("Hello ", name)

# # sayHello = greeting

# # print(sayHello("ali"))
# # print(greeting("ali"))

# def outer(num1):
#     print("outer")
#     def inner_increment(num1):
#         print("inner")
#         return num1 + 1
#     num2 = inner_increment(num1)
#     print(num1, num2)
    

# outer(10)

def factorial(number):

    if not isinstance(number, int):
        raise TypeError("Number must be integer")
    if not number >=0:
        raise ValueError("Number must be zero or positive")

    def inner_factorial(number):
        if number <=1:
            return 1
    
        return number * inner_factorial(number-1)
    return inner_factorial(number)

print(factorial(5))








