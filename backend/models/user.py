class User:
    def __init__(self,username:str,name:str,money_paid_in:float,id=None):
        self.username = username
        self.name = name
        self.currency = "USD"
        self.money_paid_in = money_paid_in
        self.money = money_paid_in
        self.id = id

    def fetch_asset_value(self):
        pass