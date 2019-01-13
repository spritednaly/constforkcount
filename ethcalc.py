#!/usr/bin/env python

import requests
import os
import ast
from math import *
from datetime import datetime
from coinmarketcap import Market
#GET /v2/ticker/ETH

def eth_calc():
	url = 'https://api.coinbase.com/v2/prices/ETH-USD/buy'
	response = requests.get(url)
	data = ast.literal_eval(response.text)
	eth_price=data['data']['amount']

# print timestamp + ETH price
now=datetime.now()
print '%02d/%02d/%04d %02d:%02d:%02d' % (now.month,now.day,now.year,now.hour,now.minute,now.second) + 'ETH = $' + float(eth_price)

while True:
	eth_input = raw_input('ETH: [type "stop" to quit]: ')
	x = eth_input*eth_price
	return x
	if reply == 'stop':
        	break
print eth_calc(eth_price)
 	
# calc = ethprice*eth_input

# conditional
  # if ethprice < 100:
    # print 'drop everything you're doing and buy!'
  # elif ethprice >100 and ethprice <250:
    # print 'patience, pet...'
  # else:
    # print 'woohoo! ETH is alive again!'
    
# UI
# swap out cb API to cmc API

def main():
	price = eth_calc()
	print price

if __name__ == "__main__":
	main()

