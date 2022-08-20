

from models.stock_wrapper import StockWrapper
from services.stock_service import StockService


stock_service = StockService()
stock_wrapper = StockWrapper(stock_service.findStock("DNN"))
