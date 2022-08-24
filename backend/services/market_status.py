import yahoo_fin.stock_info as si

class MarketStatus:

    def get_market_status():
        res = si.get_market_status()
        print(res)
        return res