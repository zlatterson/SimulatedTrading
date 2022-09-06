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

# user = User("Medo","Medo",100000,100000)
# user_repository.save(user)

# user2 = User("Test_Account","Test_Account1",100000,100000)
# user_repository.save(user2)

stock = StockService.find_stock_price("RBLX")
print(stock)