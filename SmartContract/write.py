import json
from web3 import Web3
from datetime import datetime

def write(ganache_url, path_to_abi, address, server_id, q):
    # ganache_url = 'http://127.0.0.1:7545'
    # path_to_abi = 'abi.json'
    # address = "0x769ec15950f154653F89A3687595df49e6Bea6dD"
    # server_id = 123

    web3 = Web3(Web3.HTTPProvider(ganache_url))
    web3.eth.defaultAccount = web3.eth.accounts[0]

    abi = json.load(open(path_to_abi))
    address = web3.toChecksumAddress(address)

    contract = web3.eth.contract(address=address,abi=abi)

    now = datetime.now()
    timestamp = datetime.timestamp(now)
    
    # Writing data to blockchain
    while True:
        if q:
            typ,data = q.get()
            contract.functions.createLog(server_id, typ, data, str(datetime.fromtimestamp(timestamp))).transact()
