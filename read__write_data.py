import json
from web3 import Web3
from datetime import datetime

ganache_url = 'http://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))
web3.eth.defaultAccount = web3.eth.accounts[0]

abi = json.load(open('abi.json'))
# print(abi)
address = "0x769ec15950f154653F89A3687595df49e6Bea6dD"
address = web3.toChecksumAddress(address)
contract = web3.eth.contract(address=address,abi=abi)
# Read data from smart contract
count = contract.functions.logCount().call()
# print(contract.functions.logs(count).call())

server_id = 123
data = "This is a sample Log."
now = datetime.now()
timestamp = datetime.timestamp(now)

tx_hash = contract.functions.createLog(server_id, data, str(datetime.fromtimestamp(timestamp))).transact()

print(contract.functions.logs(count+1).call())