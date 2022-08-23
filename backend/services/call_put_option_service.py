from yahoo_fin import options

class CallPutOptionService:

    def __init__(self,ticker):
        self.ticker = ticker
    
    def find_calls(ticker):
        return options.get_calls(ticker)

    def find_puts(ticker):
        return options.get_puts(ticker)

    def find_contract(contract_name):
        return options.get_options_chain(contract_name)