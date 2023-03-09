import json

class User:
    def __init__(self):
        self.username=""
        self.password=""
        self.database = []


    def UserRegister(self):
        while True:
            self.username = input("Username: ")
            if self.username == "":
                print("You cannot type an empty value.")
            else:
                break
        while True:
            self.password = input("Password: ")
            if self.password == "":
                print("You cannot type an empty value.")
            else:
                break
        self.database = [{"username":self.username, "password":self.password}]
        while True:
            try:
                with open("user.json","r") as f:
                    self.userInfo = json.load(f)
                    break
            except:
                with open("user.json","w") as f:
                    f.write('"[]"')
        self.userInfo = json.loads(self.userInfo)
        self.userInfo.extend(self.database)
        self.userInfo = json.dumps(self.userInfo)
        with open("user.json","w") as f:
            json.dump(self.userInfo, f)

    def UserLogin(self):
        while True:
            self.usernameControl = input("Username: ")
            if self.usernameControl == "":
                print("You cannot type an empty value.")
            else:
                break
        while True:
            self.passwordControl = input("Password: ")
            if self.passwordControl == "":
                print("You cannot type an empty value.")
            else:
                break
        try:
            with open("user.json","r") as f:
                self.userInfo = json.load(f)
        except:
            print("JSON File is not found. Please register again.")
        self.userInfo = json.loads(self.userInfo)
        for self.controlInfo in self.userInfo:
            if self.controlInfo["username"]==self.usernameControl and self.controlInfo["password"]==self.passwordControl:
                print("Successful login")
                break
        else:
            print("Wrong Login")

while True: # Launching part of app
    print(" Menu ".center(50,"*"))
    choice = int(input("1- User Register\n2- User Login\n3- Quit\nChoice: "))
    if choice==1:
        User().UserRegister()
    elif choice==2:
        User().UserLogin()
    elif choice==3:
        print("Quiting the application..")
        break
    else:
        print("Wrong choice")

