class User:
    def __init__(self,username,name,money_paid_in,money,id=None):
        self.username = username
        self.name = name
        self.money_paid_in = money_paid_in
        self.money = money
        self.currency = "USD"
        self.id = id



    def fetch_asset_value(self):
        pass
    # @property 
    # def money_available(self):
    #     profit = self.money_paid_in - self.money
    #     return self.money + self.money_paid_in