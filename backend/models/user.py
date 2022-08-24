class User:
    def __init__(self,username:str,name:str,money:float,id=None):
        self.username = username
        self.name = name
        self.currency = "USD"
        self.money = money
        self.id = id