import pdb, time, sys
from binance.client import Client
from binance.exceptions import BinanceOrderException, BinanceAPIException

api_key = 'your_api_key'
api_secret = 'your_api_secret'
pairing = 'ETHBTC'
spend = 0.05  # in BTC

def buy_order(client, price):
    # place a test market buy order, to place an actual order use the create_order function
    try:
        quant = int(spend/float(price))
        order = client.create_order(
            symbol=pairing,
            side=Client.SIDE_BUY,
            type=Client.ORDER_TYPE_MARKET,
            quantity=quant)
        print ('[!] Bought '+str(quant)+' [!]')
        return True
    except (BinanceOrderException, BinanceAPIException):
        # Retry API exceptions
        time.sleep(5)
        buy_order(client, price)
    except:
        return False

def search_for_coin():

    try:
        #initiate client
        client = Client(api_key, api_secret)

        #get balance
        #balance = client.get_asset_balance(asset='BTC')

        # get all symbol prices
        prices = client.get_all_tickers()

        # find coin
        for coin in prices:
            if coin['symbol'] == pairing:
                print ('[!] Pairing Found [!]')
                price = coin['price']
                print ('[!] Pairing Price: ' + price + 'BTC [!]')
                created_order = buy_order(client, price)
                if created_order is True:
                    return True
                else:
                    print ('[!] ERROR! Retrying... [!]')

        return False

    except (KeyboardInterrupt, SystemExit):
        # debug
        raise

if __name__== "__main__":
    print ('[+] Searching for '+pairing+' ... [+]')
    time_waited = 0
    found = False
    while found_coin is False:
        sys.stdout.flush()
        found = search_for_coin()
        if found is False:
            time.sleep(30)
            time_waited += 30
            if time_waited % 3600 == 0:
                print('[-] Retrying, waited for ' + str((time_waited/60) + ' hours [-]'))
        else:
            print('Complete')
            sys.exit()
