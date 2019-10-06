
from bs4 import BeautifulSoup
import requests
import quandl
import math 
import BondsModel
page_link = "https://data.treasury.gov/feed.svc/DailyTreasuryYieldCurveRateData?$filter=month(NEW_DATE)%20eq%207%20and%20year(NEW_DATE)%20eq%202019"
# this is the url 
page_response = requests.get(page_link, timeout=5)
# here, we fetch the content from the url, using the requests library
page_content = BeautifulSoup(page_response.content, "html.parser")
#we use the html parser to parse the url content and store it in a variable.
prices = page_content.find_all(title="DailyTreasuryYieldCurveRateDatum")

contract = eval(input("\x1b[1;32m Choose the type of the contract \n 1) Futures \t 2) Forwards \n 3) Government issued Zero Copoun Bonds \t 4) Government issued Non- Zero Copoun Bonds \n"))
#EIA/PET_RWTC_D    WGC/GOLD_DAILY_USD
comm = eval(input("Enter the underlying commodity of the contract \n 1) Gold \t 2) Oil \n 3) English Pound \t 4) Wheat \n"))
commodity = ""
if(comm == 1):
	commodity = "WGC/GOLD_DAILY_USD"
elif(comm == 2):
	commodity = "EIA/PET_RWTC_D"
elif(comm == 3):
	commodity = "CUR/GBP"
elif(comm == 4):
	commodity = "ODA/PWHEAMT_USD"


if(contract == 1):
	Spotprice = quandl.get("EIA/PET_RWTC_D",rows=1,returns= "numpy")
	x = eval(input("Enter the number of days till excercising of the contract \n"))
	Futuresprice = Spotprice[0][1] * (1+ 0.028*(x/365))
	print(Futuresprice)

elif(contract ==2):
	Spotprice = quandl.get("BMA/GOLD",rows=1,returns= "numpy")
	x = eval(input("Enter the delivery date in years"))
	forwardprice = Spotprice[0][1] * math.exp(0.028*x)
	print(forwardprice)
elif(contract ==3):
  BondsModel.priceZer0()
	print( "Zero Copoun Bond")


elif(contract == 4):
	BondsModel.priceCopoun()
	print("Copoun Bond")




#def webscrape():
