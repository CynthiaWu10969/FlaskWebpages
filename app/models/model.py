stocks_chart = [
 {'symbol': "AAPL", 'year': "1990", 'price': 100}, 
 {'symbol': "AAPL", 'year': "2000", 'price': 2.87},
 {'symbol': "AAPL", 'year': "2008", 'price': 17.83},
 {'symbol': "AAPL", 'year': "2019", 'price': 210.48},
 {'symbol': "VZ", 'year': "1990", 'price': 	6.07},
 {'symbol': "VZ", 'year': "2000", 'price': 20.28},
 {'symbol': "VZ", 'year': "2008", 'price': 19.17},
 {'symbol': "VZ", 'year': "2019", 'price': 57.01}
 # {'symbol': "FB", 'year': "1990"}, 'price':
 # {'symbol': "FB", 'year': "2000"}, 
 # {'symbol': "FB", 'year': "2008"}, 
 # {'symbol': "FB", 'year': "2019", 'price': 195.74}, 
 # {'symbol': "TSLA", 'year': "1990"}, 
 # {'symbol': "TSLA", 'year': "2000"}, 
 # {'symbol': "TSLA", 'year': "2008"}, 
 # {'symbol': "TSLA", 'year': "2019", 'price': 195.74}, 
 # {'symbol': "MSFT", 'year': "1990"}, 
 # {'symbol': "MSFT", 'year': "2000"}, 
 # {'symbol': "MSFT", 'year': "2008"},
 # {'symbol': "MSFT", 'year': "2019", 'price': 141.06}
 ]
  
  
# make sure to store different years as different dictionaries even for the same stock
#one price for every dictionary

def shares_calculator(symbol, initial_balance, initial_year):
    initial_price = 0
    for stock in stocks_chart:
        if (symbol == stock['symbol']) and (initial_year == stock['year']):
            initial_price = stock['price']
    shares_all = initial_balance // initial_price
    return shares_all
    
def balance_calculator(shares_all, shares, symbol, initial_balance, initial_year, sell_year):
    for stock in stocks_chart:
        if (symbol == stock['symbol']) and (initial_year == stock['year']):
            initial_price = stock['price']
    if shares < shares_all:
        for stock in stocks_chart:
            if (sell_year == stock['year']) and (symbol == stock['symbol']):
                sell_price = stock['price']
        profit = (sell_price - initial_price) * shares
        balance = initial_balance + profit
        return balance
    else:
        return "Please enter a valid shares"
        
# print(shares_calculator('AAPL', 2900, "1990"))
# print(balance_calculator(29, 25, 'AAPL', 2900, "1990", "2019"))