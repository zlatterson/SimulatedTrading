from services.call_put_option_service import CallPutOptionService
from services.stock_service import StockService

import yahoo_fin.stock_info as si
# info = si.get_market_status()
# print(info)

res = CallPutOptionService.find_contract("GOOGL220902C00060000")
print(res)