class WebsiteLogin:
    "parent"
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
    def loginInfo(self):
        print(self.name + " " + self.surname)
        
class IdsLogin(WebsiteLogin):
    "child"
    def __init__(self, name, surname, ids):
        WebsiteLogin.__init__(self, name, surname)
        self.ids = ids
        
    def login(self):
        print(self.name + " " + self.surname + " " + self.ids)
        
class EmailLogin(WebsiteLogin):
    "child"
    def __init__(self, name, surname, email):
        WebsiteLogin.__init__(self, name, surname)
        self.email = email
        
    def login(self):
        print(self.name + " " + self.surname + " " + self.email)