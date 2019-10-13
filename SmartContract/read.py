import json
from web3 import Web3
from datetime import datetime

def read(ganache_url, path_to_abi, address, server_id, count):
    # ganache_url = 'http://127.0.0.1:7545'
    # path_to_abi = 'abi.json'
    # address = "0x769ec15950f154653F89A3687595df49e6Bea6dD"
    # server_id = 123

    web3 = Web3(Web3.HTTPProvider(ganache_url))
    web3.eth.defaultAccount = web3.eth.accounts[0]

    abi = json.load(open(path_to_abi))
    address = web3.toChecksumAddress(address)

    contract = web3.eth.contract(address=address,abi=abi)
    
    # Index of data on blockchain
    index = contract.functions.logCount().call()
    
    # Reading data from blockchain
    while index and count:
        print(contract.functions.logs(index).call())
        index -= 1
        count -= 1