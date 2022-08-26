class User:
    def __init__(self,username,name,money_paid_in,money=None,id=None):
        self.username = username
        self.name = name
        self.currency = "USD"
        self.money_paid_in = money_paid_in
        self.money = money_paid_in
        self.id = id

    def fetch_asset_value(self):
        pass
    # @property 
    # def money_available(self):
    #     profit = self.money_paid_in - self.money
    #     return self.money + self.money_paid_in