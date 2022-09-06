class User:
    def __init__(self,username:str,name:str,money_paid_in:float,money:float,id=None):
        self.username = username
        self.name = name
        self.money_paid_in = money_paid_in
        self.money = money
        self.currency = "USD"
        self.id = id