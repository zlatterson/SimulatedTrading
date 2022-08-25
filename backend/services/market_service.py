import yahoo_fin.stock_info as si

class MarketService:

    def market_open():
        if si.get_market_status() != "REGULAR":
            raise Exception("Market is not open")
        return