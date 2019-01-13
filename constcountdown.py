#!/usr/bin/env python
  
""" 
create a realtime countdown counter for the Constantinople fork @ block #7080000
 (1) pull latest block from Infura
 (2) subtract block # from 7080000 
 (3) refresh results hourly
"""

import requests
import json
import os
import ast
from math import *
from datetime import datetime

# query block height through json-rpc infura api
def get_blocknumber():
	# unique project ID endpoint; remember to enclose with quotation marks
	url = 'https://mainnet.infura.io/v3/cf03c330264a4bc5974a288edc5e4560'
	
	headers = {
		'content-type': 'application/json',
	}
	
	data = {
		"jsonrpc":"2.0",
		"method":"eth_blockNumber",
		"params": [],
		"id":1
	}

	response = requests.post(url, headers=headers, data=json.dumps(data))
	request_result = response.json()
	# pull result key from response; returns hex value
	block_hex = request_result["result"]
	# convert hex value into integer
	block_height = int(block_hex,0)
	return block_height

# Subtract latest block from Constantinople fork
def block_calc(block_height):
	# Block 7080000
	const_block = 7080000 - int(block_height)
	now=datetime.now()
	print '%02d/%02d/%04d %02d:%02d:%02d || %s remaining blocks until Constantinople fork' % (now.month,now.day,now.year,now.hour,now.minute,now.second,const_block)
	return const_block

def main():

	current_block = get_blocknumber()
	block_calc(current_block)


if __name__ == "__main__":
	main() 
