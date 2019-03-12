#!/usr/bin/env python
  
""" 
Calculate remaining blocks to Constantinople fork
 (1) pull latest block # from Infura api
 (2) countdown block # from 7280000 
 (3) output remaining block count
"""

import requests
import json
import os
import ast
import settings
from math import *
from datetime import datetime

# query block height through json-rpc infura api
def get_blocknumber():
    # unique project ID endpoint; remember the quotation marks
    url = settings.url

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
    # Block 7280000
    if block_height <= 7280000:
        const_block = 7280000 - int(block_height)
        now=datetime.now()
        print '%s remaining blocks until Constantinople fork! || %02d/%02d/%04d %02d:%02d:%02d' % (const_block,now.month,now.day,now.year,now.hour,now.minute,now.second)
    else:
        print 'Forked!'
    return const_block

def main():

    current_block = get_blocknumber()
    block_calc(current_block)

if __name__ == "__main__":
    main()

