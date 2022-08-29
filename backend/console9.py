from services.stock_service import StockService

import yahoo_fin.stock_info as si
info = si.get_market_status()
print(info)