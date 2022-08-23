import yahoo_fin.stock_info as si

class ApiStatus:

    def __init__(self,test_ticker):
        self.test_ticker = test_ticker

    def get_market_status():
        res = si.get_market_status()
        print(res)
        return res