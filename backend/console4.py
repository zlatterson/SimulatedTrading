from time import sleep
from models.user import User
from services.buy_sell_action_service import BuySellActionService
from services.call_put_contract_service import CallPutContractService
from services.stock_service import StockService
from models.stock import Stock
from pprint import pprint
 

import repositories.stock_repository as stock_repository
import repositories.call_put_contract_repository as call_put_contract_repository

stock_repository.delete_all()
call_put_contract_repository.delete_all()

google_stock = StockService.make_stock("GOOGL")
stock_repository.save(google_stock)
googl = stock_repository.select(1)

call = CallPutContractService.make_contract("GOOGL220826C00055000",googl,"CALL")
call_put_contract_repository.save(call)

all_calls = call_put_contract_repository.select_all()
for c in all_calls:
    c.fetch_c_price()
    pprint(vars(c))

print("___")

specific_call = call_put_contract_repository.select(1)
specific_call.fetch_c_price()
pprint(vars(specific_call))