from datetime import date
import pycoingecko

curr_date = str(date.today())
curr_date = curr_date[8:] + "-" + curr_date[5:7] + "-" + curr_date[0:4]

# აქ შეგიძლიათ შეამოწმოთ, მხოლოდ ბოლო 365 დღის განმავლობაში შეძენილ ბიტკოინის ფასსა 
# და მიმდინარე ფასს შორის განსხვავება

date_str = input("Write the date (example:'dd-mm-yyyy'), when you bought the bitcoin: ")

# Initialize CoinGecko API client
coinGecko = pycoingecko.CoinGeckoAPI()

btc_data = coinGecko.get_coin_history_by_id(id='bitcoin', date=date_str)
price = round(btc_data['market_data']['current_price']['usd'])

btc_data_current = coinGecko.get_coin_history_by_id(id='bitcoin', date=curr_date)
current_price = round(btc_data_current['market_data']['current_price']['usd'])

if(price > current_price):
    print("You lost",price - current_price,"$")
else:
    print("You won",current_price - price,"$")
