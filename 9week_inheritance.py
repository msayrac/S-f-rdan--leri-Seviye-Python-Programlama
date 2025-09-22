
# inheritance (kalıtım) : miras alma

class Person():

    def __init__(self,name,lname):
        self.name = name
        self.lname = lname
        print("person created")
    
    def who_am_i(self):
        print("I am a person")

    def eat(self):
        print("I am eating")


class Student(Person):
    def __init__(self,name,lname, number):

        Person.__init__(self,name,lname)
        self.number = number

        print("student created")
    
    #override
    def who_am_i(self):
        print("I am a student")

    def say_hello(self):
        print("hello I am a student")

class Teacher(Person):
    def __init__(self,name,lname,branch):
        super().__init__(name,lname) 
        self.branch = branch
    
    def who_am_i(self):
        print(f"I am  {self.branch} teacher")

p1 = Person("ali","yılmaz")

s1 = Student("ccınar","turan",123456)

t1= Teacher("Mehmet","Kaya","Fizik")
print(p1.name, p1.lname)
print(s1.name, s1.lname, s1.number)

p1.who_am_i()
s1.who_am_i()


p1.eat()
s1.eat()

s1.say_hello()

t1.who_am_i()
