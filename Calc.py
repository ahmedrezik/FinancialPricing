import warnings
from optionClass import generic_option
from yahoo_fin import stock_info as si
import stock_vol

#The ticker of the comapnies' stocks we are buying options on
ticker = eval(input("\x1b[1;32m Enter the underlying stock trading ticker \n \n some famous tickers: \n Google: GOOGL \t Apple: AAPL \n Tesla: TSLA \t Amazon: AMZN\n Netflix: nflx \t Ford Motors: F \n"))

S0 =si.get_live_price(ticker)

op = eval(input("  What is the type of the Option?(American Put = 1, American Call = 2, European Put = 3, European Call = 4) \n"))
print("The current price is " ,S0 "\n", stock_vol.mean_sigma())
K= eval(input("Enter the Option Strike Price\n \n"))

print("The risk free rate is ~ 0.0208 ~ scraped from the US treasurey and Bonds website \n")

length = eval(input("Time to maturity of the option contract (in years): \n"))

N = eval(input("Number of Periods of the contract (ceiled Integer)\n"))



type = True
if(op == 1 or op == 2):
	type = False


stock_opp = generic_option(500,K,0.0208,length,N,{'tk': ticker, 'start': '2017-08-18',
                                                     'end': '2018-08-18', 'eu_option':type})


# option_eu = euro_option(217.58, 215, 0.05, 0.1, 40, {'tk': 'AAPL', 'start': '2017-08-18',
#                                                      'end': '2018-08-18', 'eu_option':False})
# option_eu2 = euro_option(217.58, 215, 0.05, 0.1, 40, {'tk': 'AAPL', 'use_garch': True, 'start': '2017-08-18',
#                                                      'end': '2018-08-18', 'eu_option':False})

print(stock_opp.price())
#print(option_eu2.price())
