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
import repositories.call_put_contract_repository as call_put_contract_repository
import repositories.call_put_option_repository as call_put_option_repository

user_repository.delete_all()
stock_repository.delete_all()
call_put_contract_repository.delete_all()
call_put_option_repository.delete_all()

user = User("Jimmy120","Jimmy",200100.123,200100.123)
user_repository.save(user)
jimmy = user_repository.select(1)

stock = StockService.make_stock("GOOGL")
stock_repository.save(stock)
googl = stock_repository.select(1)
googl.fetch_price()

call = CallPutContractService.make_contract("GOOGL220826C00055000",googl,"CALL")
call_put_contract_repository.save(call)
googl_call = call_put_contract_repository.select(1)
googl_call.fetch_c_price()

call_position = CallPutOptionService.make_position(googl_call,"BUY",3,jimmy)
pprint(vars(call_position))
call_put_option_repository.save(call_position)

# all_call_poss = call_put_option_repository.select_all()
# for c in all_call_poss:
#     pprint(vars(c))
# pprint(vars(call_position))

specifc_call_pos = call_put_option_repository.select(1)
pprint(vars(specifc_call_pos))

# specifc_call_pos.n_contracts = 12301
# call_put_option_repository.update(specifc_call_pos)