
class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email 

class UserRepository:
    def __init__(self):        
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

        # load user from .json file
        self.loadUser()
    def loadUser(self):
        pass


    def register(self,user :User):
        self.users.append(user)
        # self.saveToFile()
        print("Kullanıcı oluşturuldu. ")



    def login(self):
        pass
    def savetoFile(self):
        pass

repository = UserRepository()


while True:
    print("Menü".center(50,"*"))
    secim = input("1- Register\n2-Login\n3- Logout\n4= identity\n5- Exit\nSeciminiz : ")

    if secim == "5":
        break
    else:
        if secim =="1":
            username = input("Username : ")
            password = input("Password : ")
            email = input("email : ")
            
            user = User(username=username,password=password, email=email)

            repository.register(user=user)

            
        elif secim =="2":
            # login
            pass
        elif secim == "3":
            # logout
            pass
        elif secim == "4":
            # display user name
            pass
        else:
            print("Yanlış Secim : ")








