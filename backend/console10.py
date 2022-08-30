from time import sleep
from models.user import User
from services.buy_sell_action_service import BuySellActionService
from services.call_put_contract_service import CallPutContractService
from services.call_put_option_service import CallPutOptionService
from services.stock_service import StockService
from models.stock import Stock
from pprint import pprint
 
import repositories.user_repository as user_repository
import repositories.stock_repository as stock_repository
import repositories.buy_sell_action_repository as buy_sell_action_repository
import repositories.call_put_contract_repository as call_put_contract_repository
import repositories.call_put_option_repository as call_put_option_repository

user = User("Jimmy120","Jimmy",200100.123,200100.123)
user_repository.save(user)

stocky = StockService.make_stock("GOOGL")
stock_repository.save(stocky)

# ----

stock = stock_repository.select_by_ticker("GOOGL")
stock.fetch_price()

contract = CallPutContractService.make_contract("GOOGL220902C00060000",stock,"CALL")
contract.fetch_c_price()
call_put_contract_repository.save(contract)

result = CallPutOptionService.make_position(contract,"BUY",10,user)
call_put_option_repository.save(result[0])
user.money = result[1].money
user_repository.update(result[1])

# result2 = BuySellActionService.make_postion(dnn,123000,"BUY",user)
# buy_sell_action_repository.save(result2[0])
# user.money = result2[1].money
# user_repository.update(result2[1])
# print(result2[1].money)